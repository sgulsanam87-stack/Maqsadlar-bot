# Maqsadlar bot

Telegram orqali har kuni namoz vaqtlari va shaxsiy maqsadlarni eslatib turadigan bot.
GitHub Actions'da kuniga 4 marta ishga tushadi (har biri 6 soatlik oynani qamraydi).

Sozlamalar (Settings → Secrets and variables → Actions):

- `TELEGRAM_TOKEN` (secret): @BotFather bergan token
- `GOALS` (secret): har qatorda bitta maqsad
- `CHAT_ID` (secret yoki variable): Telegram chat id. "setup" rejimida aniqlanadi
- `CITY` (variable, ixtiyoriy): shahar nomi, masalan `Toshkent`. Standart: `Samarqand`

Sinab ko'rish: Actions → Eslatmalar → Run workflow → `test`.
