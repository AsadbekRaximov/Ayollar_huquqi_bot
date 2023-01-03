import logging
from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
API_TOKEN = ''
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Assalomu alaykum", reply_markup=main_menu)


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("""Bot test rejimida ishlamoqda!
Taklif va mulohazalar uchun: @RahimovAsadbek""")


# --------------- 1 OILAVIY MUNOSABATLAR --------------
@dp.message_handler(text="👨‍👩‍👧‍👦 Oilaviy munosabatlar")
async def handler(message: types.Message):
    await message.answer("👨‍👩‍👧‍👦 Oilaviy munosabatlar bo'limi", reply_markup=oilaviy_munosabatlar_menu)


@dp.message_handler(text="🔙 Bosh menu")
async def handler(message: types.Message):
    text="""Bosh menu"""
    await message.answer(text, reply_markup=main_menu)


# ======== 1.1 NIKOHNI BEKOR QILISH ============
@dp.message_handler(text="Nikohni bekor qilish")
async def handler(message: types.Message):
    text="""Nikohni bekor qilish bo'limi"""
    await message.answer(text, reply_markup=nikohni_bekor_menu)


@dp.message_handler(text="Bekor qilish tartibi")
async def handler(message: types.Message):
    text="""
    Batafsil:
    https://telegra.ph/Nikohni-bekor-qilish-tartibi-12-23"""
    await message.answer(text)


@dp.message_handler(text="Bir tomon arizasi asosida bekor qilish")
async def handler(message: types.Message):
    text="""
Quyidagi hollarda er yoki xotindan birining arizasi asosida nikohdan ajratish qayd etiladi
sud tomonidan bedarak yo‘qolgan deb topilgan bo‘lsa;
sud tomonidan ruhiyati buzilishi (ruhiy kasalligi yoki aqli zaifligi) sababli muomalaga layoqatsiz deb topilgan bo‘lsa;
sodir qilgan jinoyati uchun uch yildan kam bo‘lmagan muddatga ozodlikdan mahrum qilingan bo‘lsa.
Vakolatli organ: FHDYo organlari

Taqdim etiladigan hujjatlar
Ariza;
Er (xotin)ning muomalaga layoqatsiz yoxud bedarak yo‘qolgan deb topilganligi to‘g‘risida qonuniy kuchga kirgan sud qarori;
Er (xotin)ning uch yildan kam bo‘lmagan muddatga ozodlikdan mahrum qilinganligi to‘g‘risida qonuniy kuchga kirgan sud hukmidan ko‘chirma;
Sudlangan er (xotin)ning nikohdan ajratishga o‘rtada bolalari va molmulki yuzasidan nizosi yo‘qligi to‘g‘risidagi roziligi.

Xizmat uchun davlat boji qonunga muvofiq undiriladi.

Muddat: Er (xotin)dan birining arizasi bo‘yicha nikohdan ajratish uning ishtirokida, FHDYo organiga ariza berilgan kundan keyin bir oy o‘tgach amalga oshiriladi.

Davlat xizmati ko‘rsatish natijasi: nikohning bekor qilinganligi haqidagi guvohnoma."""
    await message.answer(text)


@dp.message_handler(text="Sud qarori asosida bekor qilish")
async def handler(message: types.Message):
    text="""
FHDYo organi sud qarori asosida er-xotinlardan birining arizasiga binoan nikohdan ajratish to‘g‘risidagi dalolatnoma yozuvini qayd etadi va nikohdan ajratish to‘g‘risidagi guvohnomani beradi.

Qonuniy kuchga kirgan nikohdan ajratishni qayd etish respublika sudlari qarorlari bilan er-xotindan birining doimiy yashash yoki vaqtincha turgan joyidagi FHDYo organi tomonidan amalga oshiriladi.
Bunda nikohdan ajratishni qayd etishgacha FHDYo organi er yoki xotindan birining nikohdan ajratilganlik fakti rasmiylashtirilganligini tekshiradi.
Tekshiruv sud qarori qonuniy kuchga kirgan kundan boshlab, murojaat etilgan kungacha nikohdan ajratish to‘g‘risidagi Alfavit daftari bo‘yicha va nikoh tuzilganligi haqidagi dalolatnoma yozuvi (nikoh bekor qilinganligi haqida belgi qo‘yilganligi yoki yo‘qligi) bo‘yicha o‘tkaziladi.
Agar nikohdan ajratish FHDYo organida tomonlardan birining arizasiga ko‘ra qayd etilgan bo‘lsa, u holda dalolatnoma yozuvi ikkinchi tomon to‘g‘risidagi ma’lumotlar bilan to‘ldiriladi va nikohdan ajratganlik to‘g‘risida guvohnoma beriladi.

Taqdim etiladigan hujjatlar
Er yoki xotindan birining nikohdan ajralishni qayd etish to‘g‘risidagi ariza;
Sudning nikohdan ajratish to‘g‘risidagi qonuniy kuchga kirgan hal qiluv qarori.

Xizmat uchun davlat boji qonunga muvofiq undiriladi.

Muddat: sud qarori kuchga kirgach.
Natija: nikohning bekor qilinganligi haqidagi guvohnoma.
FHDYo organlari haqida ma’lumot olish uchun quyidagi havolaga o‘ting.
FHDYo organi qabuliga yozishi uchun havolaga o‘ting."""
    await message.answer(text)


@dp.message_handler(text="O'zaro rozilik asosida bekor qilish")
async def handler(message: types.Message):
    text="""
Alohida yashovchi er-xotinni nikohdan ajratishni qayd etish ularning birgalikda bergan arizalariga asosan, ulardan birining doimiy yashash yoki vaqtincha turgan joyidagi FHDYo organi tomonidan amalga oshiriladi.

Agar er-xotindan biri nikohdan ajralish to‘g‘risidagi arizani berish uchun FHDYo organiga kela olmasa, u holda er-xotin nomidan birgalikda yozilgan arizani ulardan biri topshirishi mumkin. Kela olmagan er yoki xotinning arizadagi imzosi notarial tartibda yoki er-xotin doimiy yashayotgan yoki vaqtincha turgan joydagi FHDYo organi mudiri tomonidan tasdiqlangan bo‘lishi kerak. Arizada er-xotin ajralishga o‘zaro rozi ekanliklari, voyaga etmagan bolalari yo‘qligi, shuningdek ulardan biri nikohdan ajratish qayd etilishi belgilangan kunda FHDYo organiga kela olmasa, nikohdan ajratishning uning ishtirokisiz qayd etilishiga roziligi tasdiqlanadi.

Taqdim etiladigan hujjatlar:
Mulkiy nizolari hamda voyaga etmagan farzandlari (shu jumladan, farzandlikka olinganlari) bo‘lmagan er-xotinlarning nikohdan ajralish to‘g‘risidagi arizasi;
Shaxsini tasdiqlovchi hujjat – pasport;
Nikoh tuzilganligi haqidagi guvohnoma.

O‘zbekiston Respublikasi fuqarolari, MDH davlatlari, fuqaroligi bo‘lmagan shaxslarning nikohdan ajratish umumiy asoslarga ko‘ra qayd etiladi.

Xizmat uchun davlat boji qonunga muvofiq undiriladi.
Muddat: FHDYo organiga ariza bergan kundan keyin uch oy o‘tgach amalga oshiriladi
Natija: nikohning bekor qilinganligi haqidagi guvohnoma.
"""
    await message.answer(text)


@dp.message_handler(text="Ajrimdan keyingi majburiyatlar")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Ajrimdan-keyingi-majburiyatlar-12-23
"""
    await message.answer(text)


# ============= 1.2 ALIMENT MASALASI =============
@dp.message_handler(text="Aliment masalasi")
async def handler(message: types.Message):
    text="Aliment bo'limi"
    await message.answer(text, reply_markup=aliment_menu)


@dp.message_handler(text="Aliment majburiyati")
async def handler(message: types.Message):
    text="""Batafsil: 
https://telegra.ph/Aliment-majburiyati-12-23"""
    await message.answer(text)


@dp.message_handler(text="Aliment to'lashda kelishuv")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Aliment-tolashda-kelishuv-12-23"""
    await message.answer(text)


@dp.message_handler(text="Alimentni sud tartibida undirish")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Alimentni-sud-tartibida-undirish-12-23"""
    await message.answer(text)


@dp.message_handler(text="Aliment to'lamaganlik uchun javobgarlik")
async def handler(message: types.Message):
    text="""
    Batafsil:
    https://telegra.ph/Aliment-tolamaganlik-uchun-javobgarlik-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Alimentni undirish")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Alimentni-undirish-12-23"""
    await message.answer(text)


@dp.message_handler(text="Alimentdan ozod qilish")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Aloimentdan-ozod-qilish-12-23"""
    await message.answer(text)



# =============== 1.3 VASIYLIKKA EGA BO'LMAGAN BOLALAR =============
@dp.message_handler(text="Vasiylikka ega bo'lmagan bolalar")
async def handler(message: types.Message):
    text="""Vasiylikka ega bo'lmagan bolalar bo'limi
    """
    await message.answer(text, reply_markup=vasiylik_menu)


@dp.message_handler(text="Farzandlikka olish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Farzandlikka-olish-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Farzandlikka olishning huquqiy oqibatlari")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Farzandlikka-olishning-huquqiy-oqibatlari-12-23
    """
    await message.answer(text)


# =========== 1.4 HORIJDAGI OILAVIY MASALALAR =========
@dp.message_handler(text="Xorijdagi oilaviy masalalar")
async def handler(message: types.Message):
    text="""Xorijdagi oilaviy masalalar bo'limi
    """
    await message.answer(text, reply_markup=xorijdagi_oila_menu)


@dp.message_handler(text="Xorijda nikohni qayd etish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Xorijda-nikohni-qayd-etish-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Xorijda tug‘ilgan bolani qayd etish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Xorijda-tugilgan-bolani-qayd-etish-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Xorijda nikohni bekor qilish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Xorijda-nikohni-bekor-qilish-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Xorijda o‘limni qayd etish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Xorijda-olimni-qayd-etish-12-23
    """
    await message.answer(text)




# ----------------- 2 OILAVIY ZO'RAVONLIK ----------------
@dp.message_handler(text="🙅‍♀️ Oilaviy zo'ravonlik")
async def handler(message: types.Message):
    text="""Oilaviy zo'ravonlik bo'limi
    """
    await message.answer(text, reply_markup=zoravonlik_menu)


@dp.message_handler(text="Zo'ravonlik turlari")
async def handler(message: types.Message):
    text="""
Zo'ravonlik turlari:
https://telegra.ph/Zoravonlik-turlari-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Tazyiq va zo'ravonlikdan himoya qilish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Ayollarni-tazyiq-va-zoravonlikdan-himoya-qilish-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Ijtimoiy reabilitatsiya qilish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Ijtimoiy-reabilitatsiya-qilish-va-moslashtirish-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Himoya orderi")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Himoya-orderi-12-23
    """
    await message.answer(text)



# !!!!!!!!!!!!!!!! 3 AYOLLAR HUQUQIY HIMOYASI !!!!!!!!!!!!!
@dp.message_handler(text="👮‍♀️ Ayollar huquqiy himoyasi")
async def handler(message: types.Message):
    text="""
Ayollar huquqiy himoyasi bo'limi
    """
    await message.answer(text, reply_markup=huquqiy_himoya_menu)


@dp.message_handler(text="Ayollarning mehnat huquqlari")
async def handler(message: types.Message):
    text="""
2019-yil 1-maydan e’tiboran quyidagilar belgilangan:
Ayollar mehnatini muayyan soha yoki kasblarda qo‘llash bo‘yicha taqiqlar bekor qilindi;
tavsiyaviy xarakterdagi ayollar sog‘lig‘iga salbiy ta’sir etishi mumkin bo‘lgan soha yoki kasblar ro‘yxati tasdiqlandi;
bola parvarishlash ta’tilining kamida 3 oyi ota tomonidan foydalanilgan taqdirda, ota yoki onadan biriga O‘zbekiston Respublikasi Mehnat kodeksining 234-moddasi tartibida qo‘shimcha bir oy nafaqa to‘lanadigan bola parvarishlash ta’tili beriladi;
2 yoshga to‘lmagan farzandini tarbiyalovchi ota-onalarning biriga ularning ish paytidagi dam olish va ovqatlanish, bolani ovqatlantirish uchun beriladigan tanaffuslar hisobidan ish beruvchi bilan kelishgan holda kun davomida foydalaniladigan tanaffus vaqtini belgilash huquqi beriladi;
ayollarning pensiya yoshiga to‘lganligi yoki qonun hujjatlariga muvofiq yoshga doir davlat pensiyasini olish huquqi vujudga kelganligi sababli ular bilan tuzilgan nomuayyan muddatli mehnat shartnomasini 60 yoshga to‘lgunga qadar yoki muddatli mehnat shartnomasini muddati tugagunga qadar ish beruvchining tashabbusiga ko‘ra bekor qilish taqiqlandi;
erkak va ayollar huquqlari tengligining buzilishi bilan bog‘liq ishlarning sudlarda ko‘rib chiqilishida ayollarga advokatlar tomonidan ko‘rsatiladigan yuridik xizmat uchun haq ularning xohishiga ko‘ra davlat hisobidan qoplanadi.
Xotin-qizlarning jamiyatdagi rolini oshirish, gender tenglik va oila masalalari bo‘yicha respublika komissiyasi tarkibi
    """
    await message.answer(text)


@dp.message_handler(text="Mehnat shartnomasini bekor qilish")
async def handler(message: types.Message):
    text="""
Homilador ayollar va 3 yoshga to‘lmagan bolasi bor ayollar bilan tuzilgan mehnat shartnomasini ish beruvchining tashabbusi bilan bekor qilishga yo‘l qo‘yilmaydi, korxonaning butunlay tugatilish hollari bundan mustasno, bunday hollarda mehnat shartnomasi ularni albatta ishga joylashtirish sharti bilan bekor qilinadi.

Mazkur ayollarni ishga joylashtirishni mahalliy mehnat organi ularni ishga joylashtirish davrida qonun hujjatlarida belgilangan tegishli ijtimoiy to‘lovlar bilan ta’minlagan holda amalga oshiradi.
Muddati tugaganligi sababli mehnat shartnomasi bekor qilingan hollarda ham ish beruvchi ko‘rsatib o‘tilgan ayollarni ishga joylashtirishi shart.
Ishga joylashtirish davrida bu ayollarning ish haqi saqlanib qoladi, biroq bu muhlat muddatli mehnat shartnomasi tugagan kundan boshlab uch oydan oshmasligi kerak.
Ayollarning pensiya yoshiga to‘lganligi yoki qonun hujjatlariga muvofiq yoshga doir davlat pensiyasini olish huquqi vujudga kelganligi sababli ular bilan tuzilgan nomuayyan muddatli mehnat shartnomasini 60 yoshga to‘lgunga qadar yoki muddatli mehnat shartnomasini muddati tugagunga qadar ish beruvchining tashabbusiga ko‘ra bekor qilish taqiqlanadi.
    """
    await message.answer(text)


@dp.message_handler(text="Ayollar mehnati qo’llanilishi taqiqlangan ishlar")
async def handler(message: types.Message):
    text="""
Mehnat sharoiti noqulay ishlarda, shuningdek er osti ishlarida ayollar mehnatini qo‘llanish taqiqlanadi, er ostidagi ba’zi ishlar (jismoniy bo‘lmagan ishlar yoki sanitariya va maishiy xizmat ko‘rsatish ishlari) bundan mustasnodir.

Ayollarning ular uchun mumkin bo‘lgan normadan ortiq yukni ko‘tarishlari va tashishlari man etiladi.
Ayollar mehnatini qo‘llanish taqiqlanadigan mehnat sharoiti noqulay ishlarning ro‘yxati hamda ular ko‘tarishlari va tashishlari mumkin bo‘lgan yuk normalarining chegarasini O‘zbekiston Respublikasi Bandlik va mehnat munosabatlari vazirligi va O‘zbekiston Respublikasi Sog‘liqni saqlash vazirligi O‘zbekiston Kasaba uyushmalari federatsiyasi Kengashi va ish beruvchilarning vakillari maslahatini olgan holda tasdiqlaydi.
    """
    await message.answer(text)



@dp.message_handler(text="Homilador va farzandlik ayollarni ishga qabul qilish")
async def handler(message: types.Message):
    text="""Homiladorligi yoki bolasi borligi sababli ayollarni ishga qabul qilishni rad etish va ularning ish haqini kamaytirish Mehnat kodeksiga ko‘ra taqiqlanadi.
Homilador ayolni yoki 3 yoshga to‘lmagan bolasi bor ayolni ishga qabul qilish rad etilgan taqdirda ish beruvchi rad etishning sabablarini ularga yozma ravishda ma’lum qilishi shart.
Mazkur shaxslarni ishga qabul qilishni rad etganlik ustidan sudga shikoyat qilinishi mumkin.
    """
    await message.answer(text)


@dp.message_handler(text="Bola parvarishi uchun ta’tillar")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Bola-parvarishi-uchun-tatillar-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Ayollarga to’liqsiz ish vaqti")
async def handler(message: types.Message):
    text="""Ayollarga to’liqsiz ish vaqti

Homilador ayolning, o‘n to‘rt yoshga to‘lmagan bolasi (o‘n olti yoshga to‘lmagan nogiron bolasi) bor ayolning, shu jumladan homiyligida shunday bolasi bor ayolning yoki oilaning betob a’zosini parvarish qilish bilan band bo‘lgan shaxsning iltimosiga ko‘ra, ish beruvchi tibbiy xulosaga muvofiq ularga to‘liqsiz ish kuni yoki to‘liqsiz ish haftasi (119-modda) belgilashga majburdir.

Nogiron bolasini tarbiyalayotgan ota-onaning biriga (vasiyga, homiyga) bola o‘n olti yoshga to‘lgunga qadar davlat ijtimoiy sug‘urtasi mablag‘lari hisobidan bir kunlik ish haqi miqdorida haq to‘lagan holda oyiga qo‘shimcha bir dam olish kuni beriladi.
    """
    await message.answer(text)


@dp.message_handler(text="Nogironligi va bolasi bor ayollar uchun ta’tillar")
async def handler(message: types.Message):
    text="""Nogironligi va bolasi bor ayollar uchun ta’tillar

12 yoshga to‘lmagan ikki va undan ortiq bolasi yoki 16 yoshga to‘lmagan nogironligi bo‘lgan bolasi bor ayollarga har yili 3 ish kunidan kam bo‘lmagan muddat bilan haq to‘lanadigan qo‘shimcha ta’til beriladi.

O‘n ikki yoshga to‘lmagan ikki va undan ortiq bolasi yoki o‘n olti yoshga to‘lmagan nogiron bolasi bor ayollarga ularning xohishiga ko‘ra, har yili o‘n to‘rt kalendarь kundan kam bo‘lmagan muddat bilan ish haqi saqlanmagan holda ta’til beriladi. Bunday ta’til yillik ta’tilga qo‘shib berilishi yoki ish beruvchi bilan kelishib belgilanadigan davrda undan alohida (to‘liq yoxud qismlarga bo‘lib) foydalanilishi mumkin.
    """
    await message.answer(text)


# ********  4 AYOLLARGA IJTIMOIY HIMOYA ********
@dp.message_handler(text="📕 Ijtimoiy himoya daftarlari")
async def handler(message: types.Message):
    text="""Ijtimoiy himoya daftarlari bo'limi
    """
    await message.answer(text, reply_markup=ijtimoiy_himoya_daftarlari)

    
@dp.message_handler(text="Ayollar daftari")
async def handler(message: types.Message):
    text="""Ayollar daftari bo'limi
    """
    await message.answer(text, reply_markup=ayollar_daftari_menu)



@dp.message_handler(text="Ayollar daftari haqida")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Ayollar-daftarlari-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Bandlikni ta'minlash")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/dagi-ayollarni-bandligini-taminlash-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Tadbirkorlik faoliyatini boshlash uchun subsidiya ajratish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Tadbirkorlik-faoliyatini-boshlash-uchun-subsidiyalar-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Turar joy ijara kompensatsiyasi to'lash va uy joyini ta'mirlash")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Ayollar-daftari-dagilarga-turar-joy-ijara-kompensatsiyasi-va-uy-joyini-tamirlash-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Moddiy yordam ko'rsatish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Ayollar-daftari-dagilarga-moddiy-yordam-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Tibbiy yordam ko'rsatish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Tibbiy-yordam-korsatish-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Yoshlar daftari")
async def handler(message: types.Message):
    text="""Yoshlar daftari bo'limi
    """
    await message.answer(text, reply_markup=yoshlar_daftari_menu)




@dp.message_handler(text="Yoshlar daftari haqida")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Yoshlar-daftari-haqida-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Bir martalik moddiy yordam")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Bir-martalik-moddiy-yordam-12-23
    """
    await message.answer(text, reply_markup=yoshlar_daftari_menu)


@dp.message_handler(text="Daftardagi yoshlarni qo'llab-quvvatlash jamg'armasi")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Yoshlarni-qollab-quvvatlash-jamgarmasi-12-23
    """
    await message.answer(text, reply_markup=yoshlar_daftari_menu)


@dp.message_handler(text="Temir daftari")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Temir-daftar-12-23
    """
    await message.answer(text)




# ============== 5 AYOLLARGA IMTIYOZLAR =========
@dp.message_handler(text="🎁 Ayollarga imtiyozlar")
async def handler(message: types.Message):
    text="""Ayollarga imtiyozlar bo'limi
    """
    await message.answer(text, reply_markup=ayollarga_imtiyozlar_menu)


@dp.message_handler(text="Mehnat munosabatlari bo'yicha imtiyozlar")
async def handler(message: types.Message):
    text="""Mehnat munosabatlari bo'yicha imtiyozlar bo'limi
    """
    await message.answer(text, reply_markup=mehnatda_imtiyozlar)


@dp.message_handler(text="Ayollarga yillik ta'tillar")
async def handler(message: types.Message):
    text="""
Homilador ayollarga va bola tuqqan ayollarga yillik ta’tillar, ularning xohishiga ko‘ra, tegishlicha homiladorlik va tug‘ish ta’tilidan oldin yoki undan keyin yoxud bolani parvarishlash ta’tilidan keyin beriladi.

14 yoshga to‘lmagan bitta va undan ortiq bolani (16 yoshga to‘lmagan nogironligi bo‘lgan bolani) tarbiyalayotgan yolg‘iz ota, yolg‘iz onaga (beva erkaklar, beva ayollar, nikohdan ajrashganlar, yolg‘iz onalarga) va muddatli harbiy xizmatni o‘tayotgan harbiy xizmatchilarning xotinlariga yillik ta’tillar, ularning xohishiga ko‘ra yoz vaqtida yoki ular uchun qulay bo‘lgan boshqa vaqtda beriladi.
12 yoshga to‘lmagan ikki va undan ortiq bolasi yoki 16 yoshga to‘lmagan nogironligi bo‘lgan bolasi bor ayollarga har yili 3 ish kunidan kam bo‘lmagan muddat bilan haq to‘lanadigan qo‘shimcha ta’til beriladi.
12 yoshga to‘lmagan ikki va undan ortiq bolasi yoki 16 yoshga to‘lmagan nogiron bolasi bor ayollarga ularning xohishiga ko‘ra, har yili o‘n to‘rt kalendarь kundan kam bo‘lmagan muddat bilan ish haqi saqlanmagan holda ta’til beriladi. Bunday ta’til yillik ta’tilga qo‘shib berilishi yoki ish beruvchi bilan kelishib belgilanadigan davrda undan alohida (to‘liq yoxud qismlarga bo‘lib) foydalanilishi mumkin.
    """
    await message.answer(text)


@dp.message_handler(text="Qisqartirilgan ish vaqti va mehnat")
async def handler(message: types.Message):
    text="""
Uch yoshga to‘lmagan bolalari bor, byudjet hisobidan moliyaviy jihatdan ta’minlanadigan muassasalar va tashkilotlarda ishlayotgan ayollarga ish vaqtining haftasiga 35 soatdan oshmaydigan qisqartirilgan muddati belgilanadi.

Ish vaqtining qisqartirilgan muddati chog‘ida mehnatiga haq har kungi to‘liq ish muddati chog‘ida tegishli toifadagi xodimlar uchun belgilangan miqdorda to‘lanadi.
Homilador ayollarni va 14 yoshga to‘lmagan bolasi (16 yoshga to‘lmagan nogironligi bo‘lgan bolasi) bor ayollarni ularning roziligisiz tungi ishlarga, ish vaqtidan tashqari ishlarga, dam olish kunlaridagi ishlarga jalb qilishga va xizmat safariga yuborishga yo‘l qo‘yilmaydi.
Shu bilan birga homilador ayollarni va uch yoshga to‘lmagan bolasi bor ayollarni tungi ishlarga jalb qilishga bunday ish ona va bolaning sog‘lig‘i uchun xavf tug‘dirmasligini tasdiqlovchi tibbiy xulosa bo‘lgan taqdirdagina yo‘l qo‘yiladi.
    """
    await message.answer(text)


@dp.message_handler(text="Homilador va bolali ayollarga yengillik")
async def handler(message: types.Message):
    text="""
Tibbiy xulosaga muvofiq homilador ayollarning ishlab chiqarish normalari, xizmat ko‘rsatish normalari kamaytiriladi yoki ular avvalgi ishlaridagi o‘rtacha oylik ish haqi saqlangan holda engilroq yoxud noqulay ishlab chiqarish omillarining ta’siridan holi bo‘lgan ishga o‘tkaziladi.

Homilador ayolga engilroq yoki noqulay ishlab chiqarish omillari ta’siridan holi bo‘lgan ish berish masalasi hal etilgunga qadar, u ana shu sababdan ishga chiqmagan barcha ish kunlari uchun o‘rtacha oylik ish haqi saqlangan holda ishdan ozod etilishi lozim.
Ikki yoshga to‘lmagan bolasi bor ayollar avvalgi ishini bajarishi mumkin bo‘lmagan taqdirda, bolasi ikki yoshga to‘lgunga qadar avvalgi ishidagi o‘rtacha oylik ish haqi saqlangan holda engilroq yoki noqulay ishlab chiqarish omillarining ta’siridan holi bo‘lgan ishga o‘tkaziladi.
    """
    await message.answer(text)


@dp.message_handler(text="Onasiz bolalarni tarbiyalovchilarga imtiyoz")
async def handler(message: types.Message):
    text="""Onasiz bolalarni tarbiyalovchi shaxslarga beriladigan kafolatlar va imtiyozlar

Ayollarga onalik bilan bog‘liq holda beriladigan kafolatlar va imtiyozlar (tungi ishlarga va ish vaqtidan tashqari ishlarga, dam olish kunlaridagi ishlarga jalb etishni va xizmat safarlariga yuborishni cheklash, shuningdek qo‘shimcha ta’tillar berish, imtiyozli ish rejimlarini o‘rnatish hamda mehnat to‘g‘risidagi qonun hujjatlari va boshqa normativ hujjatlarda belgilangan boshqa kafolatlar va imtiyozlar), onasiz bolalarni (ona vafot etgan, onalik huquqlaridan mahrum etilgan, uzoq vaqt davolash muassasalarida bo‘lgan va bolalari to‘g‘risida ona sifatida g‘amxo‘rlik qilmagan boshqa hollarda) tarbiyalayotgan otalarga, shuningdek voyaga etmagan bolalarning vasiylariga (homiylariga) ham tatbiq etiladi.
Ushbu ko‘rsatilgan kafolatlar va imtiyozlar, shuningdek ota-ona g‘amxo‘rligidan mahrum bo‘lgan bolalarni amalda tarbiya qilayotgan buviga, buvaga yoki boshqa qarindoshlarga ham beriladi.
    """
    await message.answer(text)


@dp.message_handler(text="AKT sohasida attestatsiya imtiyoz")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/AKT-sohasida-attestatsiyaga-imtiyoz-12-23
    """
    await message.answer(text)


@dp.message_handler(text="Pedagoglar uchun yillik ta'til")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Pedagoglar-uchun-yillik-tatil-12-23
    """
    await message.answer(text)



@dp.message_handler(text="Jinoiy javobgarlik bo'yicha imtiyozlar")
async def handler(message: types.Message):
    text="""Jinoiy javobgarlik bo'yicha imtiyozlar bo'limi
    """
    await message.answer(text, reply_markup=jinoiy_javobgarlikda_imtiyozlar)


@dp.message_handler(text="Majburiy jamoat ishlari")
async def handler(message: types.Message):
    text="""Majburiy jamoat ishlari mahkumni haq to‘lanmaydigan foydali jamoat ishlarini bajarishga majburiy tarzda jalb qilishdan iboratdir. Mahkum ishlayotgan yoki o‘qiyotgan bo‘lsa, majburiy jamoat ishlari ishdan yoki o‘qishdan bo‘sh vaqtda o‘taladi.

Mahkumlar majburiy jamoat ishlarini o‘tashi mumkin bo‘lgan joylar (ob’ektlar) va majburiy jamoat ishlarining turi mazkur jazoning ijrosini nazorat qiluvchi organlar tomonidan belgilanadi.

Majburiy jamoat ishlari 120 soatdan 480 soatgacha bo‘lgan muddatga tayinlanadi va olti oy davomida kuniga 4 soatdan ko‘p bo‘lmagan vaqtda, mahkumga bog‘liq bo‘lmagan holatlar yuzaga kelgan taqdirda esa, bir yilgacha bo‘lgan muhlatda kuniga to‘rt soatdan ko‘p bo‘lmagan vaqtda o‘taladi.

Majburiy jamoat ishlari pensiya yoshiga etgan shaxslarga, 16 yoshga to‘lmagan shaxslarga, homilador ayollarga, 3 yoshga to‘lmagan bolalari bor ayollarga, birinchi va ikkinchi guruh nogironligi bo‘lgan shaxslarga, harbiy xizmatchilarga, chet el fuqarolariga va O‘zbekiston Respublikasida doimiy yashamaydigan shaxslarga nisbatan qo‘llanilmaydi.
    """
    await message.answer(text)


@dp.message_handler(text="Axloq tuzatish ishlari")
async def handler(message: types.Message):
    text="""Axloq tuzatish ishlari shaxs ish haqining o‘n foizidan o‘ttiz foizigacha miqdorini davlat daromadi hisobiga ushlab qolgan holda uni mehnatga majburan jalb qilishdan iborat bo‘lib, jazo sudning hukmiga muvofiq mahkumning o‘z ish joyi yoki mazkur jazo ijrosini nazorat qiluvchi organlar belgilab beradigan boshqa joylarda o‘taladi.

Axloq tuzatish ishlari olti oydan uch yilgacha muddatga tayinlanadi.
Axloq tuzatish ishlari pensiya yoshiga etganlarga, mehnatga qobiliyatsizlarga, homilador ayollarga, 3 yoshga to‘lmagan bolalari bor ayollarga va harbiy xizmatchilarga nisbatan qo‘llanilmaydi.
    """
    await message.answer(text)


@dp.message_handler(text="Ozodlikdan mahrum qilish")
async def handler(message: types.Message):
    text="""Ozodlikdan mahrum qilish mahkumni jamiyatdan ajratib jazoni ijro etish koloniyasi yoki turmaga joylashtirishdan iboratdir.

Ozodlikdan mahrum qilish bir oydan 20 yilgacha muddatga belgilanadi.
Uzoq muddatli ozodlikdan mahrum qilish yigirma yildan ortiq, lekin 25 yildan ko‘p bo‘lmagan muddatga belgilanadi va faqat javobgarlikni og‘irlashtiradigan holatlarda qasddan odam o‘ldirish (97-moddaning ikkinchi qismi) va terrorizm (155-moddaning uchinchi qismi) uchun tayinlanishi mumkin.
Uzoq muddatga ozodlikdan mahrum qilish jazosi ayolga, 18 yoshga to‘lmasdan jinoyat sodir etgan shaxsga va oltmish yoshdan oshgan erkakka nisbatan tayinlanishi mumkin emas.
    """
    await message.answer(text)


@dp.message_handler(text="Boshqa sohalar bo'yicha imtiyozlar")
async def handler(message: types.Message):
    text="""Boshqa sohalar bo'yicha imtiyozlar bo'limi
    """
    await message.answer(text, reply_markup=boshqa_sohalarda_imtiyozlar)


@dp.message_handler(text="O'qishga kirish uchun grantlar")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Oqishga-kirish-uchun-grantlar-12-23
"""
    await message.answer(text)


@dp.message_handler(text="Arzon uy-joylar berish tartibi")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Arzon-uy-joylar-berish-tartibi-12-23"""
    await message.answer(text)



@dp.message_handler(text="Pensiyaga chiqish bo'yicha imtiyozlar")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Pensiyaga-chiqish-boyicha-imtiyozlar-12-23"""
    await message.answer(text)



@dp.message_handler(text="Tadbirkor ayollarga kreditlar ajratish")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Tadbirkor-ayollarga-kreditlar-ajratish-12-23"""
    await message.answer(text)



@dp.message_handler(text="Imtiyozli ipoteka krediti")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Imtiyozli-ipoteka-krediti-12-23"""
    await message.answer(text)



@dp.message_handler(text="O'qish uchun kontrakt to'lab berish")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Oqish-uchun-kontrakt-tolab-berish-12-23"""
    await message.answer(text)



@dp.message_handler(text="Nogiron farzandliklarga soliq imtiyozi")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Nogiron-fazandi-bor-ota-onalarga-soliq-imtiyozlari-12-23"""
    await message.answer(text)



@dp.message_handler(text="Mol-mulk solig'i uchun imtiyozlar")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Mol-mulk-soligi-uchun-imtiyozlar-12-23"""
    await message.answer(text)


@dp.message_handler(text="O'qishga kirish uchun tavsiyanoma")
async def handler(message: types.Message):
    text="""Batafsil:
https://telegra.ph/Oqishga-kirish-uchun-tavsiyanoma-12-23"""
    await message.answer(text)


@dp.message_handler(text="Magistratura uchun kontrakt to'lab berish")
async def handler(message: types.Message):
    text="""
Batafsil:
https://telegra.ph/Magistratura-uchun-kontrakt-tolab-berish-12-23"""
    await message.answer(text)


@dp.message_handler()
async def handler(message: types.Message):
    text="""Noto'g'ri buyruq berdingiz!
Botni qaytadan ishga tushirish: /start"""
    await message.answer(text)


@dp.message_handler(content_types=types.ContentType.ANY)
async def handler(message: types.Message):
    text="""Noto'g'ri kontent yubordingiz!
Botni qaytadan ishga tushirish: /start"""
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)