from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# ======= 0.0 MAIN MENU ========
main_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("👨‍👩‍👧‍👦 Oilaviy munosabatlar"),
        KeyboardButton("🙅‍♀️ Oilaviy zo'ravonlik")
    ],
    [
        KeyboardButton("👮‍♀️ Ayollar huquqiy himoyasi"),
        KeyboardButton("📕 Ijtimoiy himoya daftarlari")
    ],
    [
        KeyboardButton("🎁 Ayollarga imtiyozlar"),
    ],
],
resize_keyboard=True)


# ========= 1. OILAVIY MUNOSABATLAR =====
oilaviy_munosabatlar_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Nikohni bekor qilish"),
        KeyboardButton("Aliment masalasi")
    ],
    [
        KeyboardButton("Vasiylikka ega bo'lmagan bolalar"),
        KeyboardButton("Xorijdagi oilaviy masalalar"),
    ],
    [
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)

# ======= 1.1 NIKOHNI BEKOR QILISH ==========
nikohni_bekor_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Bekor qilish tartibi"),
        KeyboardButton("Bir tomon arizasi asosida bekor qilish")
    ],
    [
        KeyboardButton("Sud qarori asosida bekor qilish"),
        KeyboardButton("O'zaro rozilik asosida bekor qilish"),
    ],
    [
        KeyboardButton("Ajrimdan keyingi majburiyatlar"),
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


# ========== 1.2 ALIMENT MASALALARI ======= 
aliment_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Aliment majburiyati"),
        KeyboardButton("Aliment to'lashda kelishuv")
    ],
    [
        KeyboardButton("Alimentni sud tartibida undirish"),
        KeyboardButton("Aliment to'lamaganlik uchun javobgarlik"),
    ],
    [
        KeyboardButton("Alimentni undirish"),
        KeyboardButton("Alimentdan ozod qilish")
    ],
    [
        KeyboardButton("🔙 Bosh menu"),
    ]
],
resize_keyboard=True)

# ========= 1.3 VASIYLIKKA EGA BO'LMAGAN BOLALAR =======
vasiylik_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Farzandlikka olish"),
        KeyboardButton("Farzandlikka olishning huquqiy oqibatlari")
    ],
    [
        KeyboardButton("🔙 Bosh menu"),
    ]
],
resize_keyboard=True)

# ======== 1.4 XORIJDAGI OILAVIY MASALALAR ======
xorijdagi_oila_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Xorijda nikohni qayd etish"),
        KeyboardButton("Xorijda tug‘ilgan bolani qayd etish")
    ],
    [
        KeyboardButton("Xorijda nikohni bekor qilish"),
        KeyboardButton("Xorijda o‘limni qayd etish"),
    ],
    [
        KeyboardButton("🔙 Bosh menu"),
    ]
],
resize_keyboard=True)


# -------------- 2. OILAVIY ZO'RAVONLIK -------------
zoravonlik_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Zo'ravonlik turlari"),
        KeyboardButton("Tazyiq va zo'ravonlikdan himoya qilish")
    ],
    [
        KeyboardButton("Ijtimoiy reabilitatsiya qilish"),
        KeyboardButton("Himoya orderi"),
    ],
    [
        KeyboardButton("🔙 Bosh menu"),
    ]
],
resize_keyboard=True)


# !!!!!!!!!!!! 3 AYOLLAR HUQUQIY HIMOYASI !!!!!!
huquqiy_himoya_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Ayollarning mehnat huquqlari"),
        KeyboardButton("Mehnat shartnomasini bekor qilish")
    ],
    [
        KeyboardButton("Ayollar mehnati qo’llanilishi taqiqlangan ishlar"),
        KeyboardButton("Homilador va farzandlik ayollarni ishga qabul qilish"),
    ],
    [
        KeyboardButton("Bola parvarishi uchun ta’tillar"),
        KeyboardButton("Ayollarga to’liqsiz ish vaqti"),
    ],
    [
        KeyboardButton("Nogironligi va bolasi bor ayollar uchun ta’tillar"),
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


# *********** 4 IJTIMOIY HIMOYA DAFTARLARI ***********
ijtimoiy_himoya_daftarlari = ReplyKeyboardMarkup([
    [
        KeyboardButton("Ayollar daftari"),
        KeyboardButton("Yoshlar daftari")
    ],
    [
        KeyboardButton("Temir daftari"),
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)

ayollar_daftari_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Ayollar daftari haqida"),
        KeyboardButton("Bandlikni ta'minlash"),
    ],
    [
        KeyboardButton("Tadbirkorlik faoliyatini boshlash uchun subsidiya ajratish"),
        KeyboardButton("Turar joy ijara kompensatsiyasi to'lash va uy joyini ta'mirlash"),
    ],
    [
        KeyboardButton("Moddiy yordam ko'rsatish"),
        KeyboardButton("Tibbiy yordam ko'rsatish")
    ],
    [
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


yoshlar_daftari_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Yoshlar daftari haqida"),
        KeyboardButton("Bir martalik moddiy yordam"),
    ],
    [
        KeyboardButton("Daftardagi yoshlarni qo'llab-quvvatlash jamg'armasi"),
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


temir_daftari_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Yoshlar daftari haqida"),
        KeyboardButton("Bir martalik moddiy yordam"),
    ],
    [
        KeyboardButton("Tadbirkorlik faoliyatini boshlash uchun subsidiya ajratish"),
        KeyboardButton("Turar joy ijara kompensatsiyasi to'lash va uy joyini ta'mirlash"),
    ],
    [
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


# ------------- 5 Ayollarga imtiyozlar -----------
ayollarga_imtiyozlar_menu = ReplyKeyboardMarkup([
    [
        KeyboardButton("Mehnat munosabatlari bo'yicha imtiyozlar"),
        KeyboardButton("Jinoiy javobgarlik bo'yicha imtiyozlar"),
    ],
    [
        KeyboardButton("Boshqa sohalar bo'yicha imtiyozlar"),
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)

mehnatda_imtiyozlar = ReplyKeyboardMarkup([
    [
        KeyboardButton("Ayollarga yillik ta'tillar"),
        KeyboardButton("Qisqartirilgan ish vaqti va mehnat"),
    ],
    [
        KeyboardButton("Homilador va bolali ayollarga yengillik"),
        KeyboardButton("Onasiz bolalarni tarbiyalovchilarga imtiyoz")
    ],
    [
        KeyboardButton("AKT sohasida attestatsiya imtiyoz"),
        KeyboardButton("Pedagoglar uchun yillik ta'til")
    ],
    [
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


jinoiy_javobgarlikda_imtiyozlar = ReplyKeyboardMarkup([
    [
        KeyboardButton("Majburiy jamoat ishlari"),
        KeyboardButton("Axloq tuzatish ishlari"),
    ],
    [
        KeyboardButton("Ozodlikdan mahrum qilish"),
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)


boshqa_sohalarda_imtiyozlar = ReplyKeyboardMarkup([
    [
        KeyboardButton("O'qishga kirish uchun grantlar"),
        KeyboardButton("Arzon uy-joylar berish tartibi"),
    ],
    [
        KeyboardButton("Pensiyaga chiqish bo'yicha imtiyozlar"),
        KeyboardButton("Tadbirkor ayollarga kreditlar ajratish")
    ],
        [
        KeyboardButton("Imtiyozli ipoteka krediti"),
        KeyboardButton("O'qish uchun kontrakt to'lab berish"),
    ],
    [
        KeyboardButton("Nogiron farzandliklarga soliq imtiyozi"),
        KeyboardButton("Mol-mulk solig'i uchun imtiyozlar")
    ],
        [
        KeyboardButton("O'qishga kirish uchun tavsiyanoma"),
        KeyboardButton("Magistratura uchun kontrakt to'lab berish"),
    ],
    [
        KeyboardButton("🔙 Bosh menu")
    ]
],
resize_keyboard=True)