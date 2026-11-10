"""Daily inspiration for the reminders: Qur'an verses, hadiths, business wisdom and useful knowledge.

Verses are given as meaning translations (ma'no tarjimasi) with surah:ayah.
Hadiths are limited to well-known narrations from the main collections, with the
collection and hadith number. Business tips and knowledge notes are practical advice
and are labelled as such, never attributed to the Prophet ﷺ or the Companions.
"""

OYAT = [
    ("Albatta, Alloh bir qavmning holatini, ular o'zlaridagi narsani o'zgartirmagunlaricha, o'zgartirmas.", "Ra'd surasi, 11-oyat"),
    ("Inson uchun faqat o'zi intilgan narsagina bordir.", "Najm surasi, 39-oyat"),
    ("Kim Allohdan qo'rqsa, U unga chiqish yo'lini qilib berur va uni o'zi o'ylamagan tomondan rizqlantirur.", "Taloq surasi, 2–3-oyatlar"),
    ("Albatta, qiyinchilik bilan birga yengillik bor. Albatta, qiyinchilik bilan birga yengillik bor.", "Sharh surasi, 5–6-oyatlar"),
    ("Qat'iy qaror qilsang, Allohga tavakkal qil. Albatta, Alloh tavakkal qiluvchilarni sevar.", "Oli Imron surasi, 159-oyat"),
    ("Alloh hech bir jonni toqatidan tashqari narsaga taklif qilmas.", "Baqara surasi, 286-oyat"),
    ("Bizning yo'limizda jihod (sa'y-harakat) qilganlarni albatta O'z yo'llarimizga hidoyat qilurmiz.", "Ankabut surasi, 69-oyat"),
    ("Va ayt: «Robbim, ilmimni ziyoda qil».", "Toha surasi, 114-oyat"),
    ("Ey iymon keltirganlar, sabr va namoz bilan yordam so'ranglar. Albatta, Alloh sabrlilar bilandir.", "Baqara surasi, 153-oyat"),
    ("Albatta, namoz fahsh va munkar ishlardan qaytarur.", "Ankabut surasi, 45-oyat"),
    ("Ba'zingiz ba'zingizni g'iybat qilmasin.", "Hujurot surasi, 12-oyat"),
    ("Yo'lga qodir bo'lgan odamlar zimmasida Alloh uchun Baytni haj qilish (farzi) bor.", "Oli Imron surasi, 97-oyat"),
    ("Orom olishingiz uchun o'zingizdan juftlar yaratib, orangizda muhabbat va rahmat paydo qilgani ham Uning oyat-alomatlaridandir.", "Rum surasi, 21-oyat"),
    ("Batahqiq, Qur'onni eslatma uchun oson qilib qo'ydik. Bas, eslatma oluvchi bormi?", "Qamar surasi, 17-oyat"),
    ("Ahlingni namozga buyur va o'zing ham unga sabrli bo'l.", "Toha surasi, 132-oyat"),
    ("Ey iymon keltirganlar, o'zingizni va ahlingizni do'zaxdan saqlang.", "Tahrim surasi, 6-oyat"),
    ("Namoz ado etilgach, yer yuzida tarqalinglar va Allohning fazlidan talab qilinglar.", "Juma surasi, 10-oyat"),
    ("O'lchov va tarozida urib qoluvchilarga halokat bo'lsin.", "Mutaffifin surasi, 1-oyat"),
    ("Alloh savdoni halol, ribo (sudxo'rlik)ni harom qildi.", "Baqara surasi, 275-oyat"),
    ("Allohning rahmatidan noumid bo'lmanglar. Albatta, Alloh barcha gunohlarni mag'firat qilur.", "Zumar surasi, 53-oyat"),
    ("Meni yod etinglar, Men ham sizlarni yod etaman. Menga shukr qilinglar, noshukrlik qilmanglar.", "Baqara surasi, 152-oyat"),
    ("Agar shukr qilsangiz, albatta sizlarga (ne'matimni) ziyoda qilurman.", "Ibrohim surasi, 7-oyat"),
    ("Robbimiz, bizga juftlarimiz va zurriyotlarimizdan ko'zimiz quvonchini ato et va bizni taqvodorlarga imom qil.", "Furqon surasi, 74-oyat"),
]

HADIS = [
    ("Amallar faqat niyatlarga bog'liqdir va har bir kishiga niyat qilgan narsasigina bordir.", "Buxoriy 1, Muslim 1907"),
    ("Allohga eng suyukli amal, oz bo'lsa ham, doimiy qilinganidir.", "Buxoriy 6464, Muslim 783"),
    ("Kuchli mo'min Allohga zaif mo'mindan yaxshiroq va suyukliroqdir. Senga foyda beradigan narsaga intil, Allohdan yordam so'ra va ojiz bo'lma.", "Muslim 2664"),
    ("Kim ilm talab qilib yo'lga chiqsa, Alloh unga jannatga yo'lni oson qilib qo'yadi.", "Muslim 2699"),
    ("Sizlarning eng yaxshingiz Qur'onni o'rgangan va uni o'rgatganingizdir.", "Buxoriy 5027"),
    ("Hech kim o'z qo'li mehnatidan yeganidan yaxshiroq taom yemagan. Allohning payg'ambari Dovud alayhissalom o'z qo'li mehnatidan yer edi.", "Buxoriy 2072"),
    ("Ayolga to'rt narsa uchun uylaniladi: moli, nasabi, jamoli va dini uchun. Dindorini tanla, qo'ling barakaga to'lsin.", "Buxoriy 5090, Muslim 1466"),
    ("Kim Allohga va oxirat kuniga iymon keltirsa, yaxshi gapirsin yoki jim tursin.", "Buxoriy 6018, Muslim 47"),
    ("G'iybat — birodaringni u yoqtirmaydigan narsa bilan eslashingdir.", "Muslim 2589"),
    ("Mabrur (qabul bo'lgan) hajning mukofoti faqat jannatdir.", "Buxoriy 1773, Muslim 1349"),
    ("Agar birortangizning eshigi oldidan daryo oqsa va u har kuni unda besh marta yuvinsa, undan kir qoladimi? Besh vaqt namoz ham shunday: Alloh ular bilan xatolarni o'chiradi.", "Buxoriy 528, Muslim 667"),
    ("Halol aniq, harom ham aniq. Ularning orasida shubhali narsalar bor. Kim shubhalidan saqlansa, dinini va obro'sini pok saqlabdi.", "Buxoriy 52, Muslim 1599"),
    ("Ikki ne'mat borki, ko'p odamlar ularda aldanib qoladi: sog'liq va bo'sh vaqt.", "Buxoriy 6412"),
    ("Kim bizni aldasa, bizdan emas.", "Muslim 102"),
    ("Sotganda, sotib olganda va haqini talab qilganda bag'rikeng bo'lgan kishiga Alloh rahm qilsin.", "Buxoriy 2076"),
    ("Kim bir yaxshilikka yo'l ko'rsatsa, unga o'sha yaxshilikni qilgan kishining ajri kabi ajr bor.", "Muslim 1893"),
    ("Rostgo'y, ishonchli savdogar payg'ambarlar, siddiqlar va shahidlar bilan birga bo'ladi.", "Termiziy 1209"),
    ("Agar Allohga haqiqiy tavakkal qilsangiz, qushlarni rizqlantirgandek sizlarni ham rizqlantirardi: ular ertalab och chiqib, kechqurun to'q qaytadi.", "Termiziy 2344"),
    ("Allohni (amrlarini) saqla, U seni saqlaydi. So'rasang, Allohdan so'ra. Yordam istasang, Allohdan iste.", "Termiziy 2516"),
    ("Alloh sizlardan biringiz bir ish qilsa, uni puxta qilishini yaxshi ko'radi.", "Bayhaqiy, Shuabul iymon (Albaniy: hasan)"),
]

BIZNES = [
    ("Abdurrahmon ibn Avf roziyallohu anhu Madinaga hijrat qilganda, ansoriy birodari unga molining yarmini taklif qildi. U esa: «Alloh molingga baraka bersin, menga bozorni ko'rsat», dedi. Savdo qilib, o'z mehnati bilan boyidi.", "Hikoya — Buxoriy 2048"),
    ("Brend — bu va'da. Har bir payvand choki mijozga «Aligarx_svarka sifatli ishlaydi» degan va'dani beradi. Bitta sifatsiz ish o'nta reklamani yo'qqa chiqaradi.", "Biznes maslahati"),
    ("Har bir tugallangan ishni suratga oling: oldin va keyin. 30 kunda 30 ta post bo'ladi — bu eng arzon va eng ishonchli reklama.", "Biznes maslahati"),
    ("Narxni aniq ayting va va'dada turing. Kelishilgan muddatda tugatilgan ish — eng yaxshi tavsiyanoma.", "Biznes maslahati"),
    ("Har bir mamnun mijozdan bitta narsa so'rang: «Tanishlaringizga tavsiya qilasizmi?» Og'zaki tavsiya — kichik biznesning eng kuchli quroli.", "Biznes maslahati"),
    ("Daromadning bir qismini har oy asbob-uskunaga ajrating. Yaxshi asbob — tez ish, tez ish — ko'p mijoz.", "Biznes maslahati"),
    ("Xavfsizlikni tejamang: niqob, qo'lqop va o'tga chidamli kiyim. Sog'lom usta — ishlaydigan biznes.", "Biznes maslahati"),
    ("Bitta yo'nalishda eng yaxshisi bo'ling (masalan, darvoza va panjaralar), keyin kengaying. Hamma narsani qiladigan usta esda qolmaydi.", "Biznes maslahati"),
    ("Har kuni kechqurun 5 daqiqa: bugun nima ishladim, qancha topdim, ertaga kimga qo'ng'iroq qilaman? Yozib qo'yilgan reja bajariladi.", "Biznes maslahati"),
    ("Mijozni kamsitmang, kichik buyurtmani ham rad etmang. Bugungi kichik mijoz ertaga katta obyektga chaqiradi.", "Biznes maslahati"),
    ("Instagram yoki Telegram sahifangizda bir xil nom, bir xil logo va bir xil telefon raqam bo'lsin. Brend — takrorlanish orqali eslab qolinadi.", "Biznes maslahati"),
    ("Halol daromad barakali bo'ladi: material sifatini yashirmang, kamchilikni oldindan ayting. Ishonch — eng qimmat kapital.", "Biznes maslahati"),
]

ILM = [
    ("Har kuni 5 oyat yod olsangiz, bir yilda 1800 dan ortiq oyat bo'ladi. Oz, lekin har kuni — Qur'on yodlashning eng ishonchli yo'li.", "Foydali ilm"),
    ("Yodlash uchun eng yaxshi vaqt — bomdoddan keyin. Yangi oyatni sunnat namozlarida takrorlasangiz, tez mustahkamlanadi.", "Foydali ilm"),
    ("Yodlangan narsa takrorlanmasa, unutiladi. Kuniga yangi yodlashdan ko'ra ko'proq vaqtni eskisini takrorlashga ajrating.", "Foydali ilm"),
    ("Yangi odat o'rtacha ikki oyda mustahkamlanadi. Birinchi haftalar qiyin bo'ladi — bu normal holat, to'xtamang.", "Foydali ilm"),
    ("Katta maqsadni kichik qadamlarga bo'ling: haj uchun har oy belgilangan summani alohida hisobga qo'yib boring.", "Foydali ilm"),
    ("Oilani namozga chorlashning eng kuchli yo'li — o'zingiz namunali bo'lishingiz. Odamlar gapdan ko'ra ko'proq ishdan o'rganadi.", "Foydali ilm"),
    ("Yaxshi uyqu — yaxshi ish. Xuftondan keyin erta yotish bomdodga turishni ham, kunduzgi ishni ham osonlashtiradi.", "Foydali ilm"),
    ("Telefonda o'tkaziladigan vaqtning bir qismini Qur'on yoki kasbiy o'rganishga bering — kuniga 20 daqiqa ham yiliga 120 soatdan ortiq bo'ladi.", "Foydali ilm"),
]


def pick(items, day, shift=0):
    text, ref = items[(day.toordinal() + shift) % len(items)]
    return f"{text}\n— {ref}"
