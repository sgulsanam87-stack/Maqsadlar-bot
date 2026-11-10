"""Maqsadlar eslatuvchi Telegram bot.

GitHub Actions runs this script four times a day. Each run covers a 6-hour
window of Uzbekistan time and sends every reminder that falls inside it:
the five prayer times, a morning goal of the day, and an evening check-in.

Environment:
  TELEGRAM_TOKEN  bot token from @BotFather (required)
  CHAT_ID         your Telegram chat id (optional; see `setup` mode)
  GOALS           one goal per line (optional; falls back to goals.txt)
  CITY            city name from CITIES below (optional, default Samarqand)
  MODE            window | test | setup | dry  (default window)
  WINDOW_START    local hour the window starts (3, 9, 15 or 21)
"""
import json
import math
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

TZ = timezone(timedelta(hours=5))
WINDOW = timedelta(hours=6)

CITIES = {
    "Toshkent": (41.2995, 69.2401), "Samarqand": (39.6542, 66.9597),
    "Buxoro": (39.7747, 64.4286), "Andijon": (40.7821, 72.3442),
    "Namangan": (40.9983, 71.6726), "Farg'ona": (40.3864, 71.7864),
    "Qo'qon": (40.5286, 70.9425), "Qarshi": (38.8606, 65.7891),
    "Navoiy": (40.0844, 65.3792), "Jizzax": (40.1158, 67.8422),
    "Guliston": (40.4897, 68.7842), "Termiz": (37.2242, 67.2783),
    "Urganch": (41.5500, 60.6333), "Nukus": (42.4600, 59.6100),
}
PRAYER_NAMES = {"bomdod": "Bomdod", "quyosh": "Quyosh", "peshin": "Peshin",
                "asr": "Asr", "shom": "Shom", "xufton": "Xufton"}
EVENING = (21, 30)  # evening check-in, local time

DEFAULT_GOALS = [
    "5 mahal namoz o'qish",
]

# ---------- prayer times (Hanafi asr, tuned to the Muslim Board of Uzbekistan table) ----------
RAD = math.pi / 180


def _fix(a, b):
    a = a - b * math.floor(a / b)
    return a + b if a < 0 else a


def _sun(jd):
    d = jd - 2451545.0
    g = _fix(357.529 + 0.98560028 * d, 360)
    q = _fix(280.459 + 0.98564736 * d, 360)
    lon = _fix(q + 1.915 * math.sin(g * RAD) + 0.020 * math.sin(2 * g * RAD), 360)
    e = 23.439 - 0.00000036 * d
    ra = math.atan2(math.cos(e * RAD) * math.sin(lon * RAD), math.cos(lon * RAD)) / RAD / 15
    decl = math.asin(math.sin(e * RAD) * math.sin(lon * RAD)) / RAD
    return decl, q / 15 - _fix(ra, 24)


def _julian(y, m, d):
    if m <= 2:
        y -= 1
        m += 12
    a = y // 100
    b = 2 - a + a // 4
    return math.floor(365.25 * (y + 4716)) + math.floor(30.6001 * (m + 1)) + d + b - 1524.5


def prayer_times(day, lat, lng):
    """Return {name: datetime} for one local date."""
    jd = _julian(day.year, day.month, day.day) - lng / (15 * 24)

    def noon(t):
        return _fix(12 - _sun(jd + t)[1], 24)

    def angle_time(angle, t, ccw=False):
        decl = _sun(jd + t)[0]
        c = (-math.sin(angle * RAD) - math.sin(decl * RAD) * math.sin(lat * RAD)) / (
            math.cos(decl * RAD) * math.cos(lat * RAD))
        tt = math.acos(max(-1, min(1, c))) / RAD / 15
        return noon(t) + (-tt if ccw else tt)

    def asr(t):
        decl = _sun(jd + t)[0]
        alt = math.atan(1 / (2 + math.tan(abs(lat - decl) * RAD))) / RAD
        return angle_time(-alt, t)

    adj = 5 - lng / 15
    hours = {
        "bomdod": angle_time(15.5, 5 / 24, True) + adj,
        "quyosh": angle_time(0.833, 6 / 24, True) + adj,
        "peshin": noon(12 / 24) + adj + 1 / 60,
        "asr": asr(13 / 24) + adj,
        "shom": angle_time(0.833, 18 / 24) + adj + 3 / 60,
        "xufton": angle_time(15.5, 18 / 24) + adj,
    }
    base = datetime(day.year, day.month, day.day, tzinfo=TZ)
    return {k: base + timedelta(minutes=round(h * 60)) for k, h in hours.items()}


# ---------- messages ----------
def load_goals():
    raw = os.environ.get("GOALS", "").strip()
    if not raw and os.path.exists("goals.txt"):
        with open("goals.txt", encoding="utf-8") as f:
            raw = f.read()
    goals = [g.strip(" -•\t") for g in raw.splitlines() if g.strip()]
    return goals or DEFAULT_GOALS


def goal_of_day(goals, day, shift=0):
    return goals[(day.toordinal() + shift) % len(goals)]


def fmt(dt):
    return dt.strftime("%H:%M")


def build_events(day, city, goals):
    lat, lng = CITIES[city]
    t = prayer_times(day, lat, lng)
    table = "\n".join(f"{PRAYER_NAMES[k]}: {fmt(v)}" for k, v in t.items())
    events = []
    for i, key in enumerate(["bomdod", "peshin", "asr", "shom", "xufton"]):
        text = f"🕌 {PRAYER_NAMES[key]} vaqti kirdi ({fmt(t[key])}, {city})."
        if key == "bomdod":
            text += (f"\n\nAssalomu alaykum! Bugungi maqsad:\n✨ {goal_of_day(goals, day)}"
                     f"\n\nBugungi namoz vaqtlari:\n{table}")
        else:
            text += f"\n\nYodingizda bo'lsin: {goal_of_day(goals, day, i)}"
        events.append((t[key], text))
    lines = "\n".join(f"▫️ {g}" for g in goals)
    evening = datetime(day.year, day.month, day.day, *EVENING, tzinfo=TZ)
    events.append((evening, "🌙 Kun yakuni. Bugun maqsadlaringiz yo'lida nima qildingiz?\n\n"
                   f"{lines}\n\nIlovada bugungi amallaringizni belgilab qo'ying."))
    return events


# ---------- telegram ----------
def tg(method, **params):
    token = os.environ["TELEGRAM_TOKEN"].strip()
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(f"https://api.telegram.org/bot{token}/{method}", data=data)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except Exception as e:  # network hiccup: retry a few times
            print(f"{method} failed ({e}), retry {attempt + 1}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    raise SystemExit(f"Telegram {method} failed")


def chat_id():
    cid = os.environ.get("CHAT_ID", "").strip()
    if cid:
        return cid
    ups = tg("getUpdates").get("result", [])
    for u in reversed(ups):
        msg = u.get("message") or u.get("edited_message")
        if msg:
            return str(msg["chat"]["id"])
    raise SystemExit("CHAT_ID topilmadi: botga Telegramda /start yozing va qayta ishga tushiring.")


def send(cid, text):
    if os.environ.get("MODE") == "dry":
        print(f"--- to {cid}\n{text}\n")
        return
    tg("sendMessage", chat_id=cid, text=text)


# ---------- main ----------
def main():
    mode = os.environ.get("MODE", "window") or "window"
    city = os.environ.get("CITY", "").strip() or "Samarqand"
    if city not in CITIES:
        raise SystemExit(f"Noma'lum shahar: {city}. Mumkin: {', '.join(CITIES)}")
    goals = load_goals()
    now = datetime.now(TZ)

    if mode == "setup":
        cid = chat_id()
        print(f"CHAT_ID={cid}")
        send(cid, "✅ Bot ulandi! Endi har kuni namoz vaqtlarida va kechqurun maqsadlaringizni eslatib turaman.")
        return
    if mode == "test":
        cid = chat_id()
        events = build_events(now.date(), city, goals)
        send(cid, "🔔 Sinov xabari. Ertalabki xabar shunday ko'rinadi:\n\n" + events[0][1])
        return

    start_hour = int(os.environ.get("WINDOW_START") or 0)
    ws = now.replace(hour=start_hour, minute=0, second=0, microsecond=0)
    if ws > now + timedelta(hours=1):  # the window started yesterday
        ws -= timedelta(days=1)
    we = ws + WINDOW
    events = []
    for d in (ws.date(), ws.date() + timedelta(days=1)):
        events += [e for e in build_events(d, city, goals) if ws <= e[0] < we]
    events.sort(key=lambda e: e[0])
    print(f"Window {ws:%Y-%m-%d %H:%M} – {we:%H:%M}: {len(events)} reminder(s)")
    if not events:
        return
    cid = chat_id() if mode != "dry" else "DRY"
    for when, text in events:
        wait = (when - datetime.now(TZ)).total_seconds()
        if mode == "dry":
            print(f"[{when:%H:%M}]", end=" ")
        elif wait > 0:
            print(f"Sleeping {wait / 60:.0f} min until {when:%H:%M}")
            time.sleep(wait)
        send(cid, text)


if __name__ == "__main__":
    main()
