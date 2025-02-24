from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ustoz_shogird.buttons.default import hayoq, menu

from ustoz_shogird.states.state_menu import UstozState

ustoz_router = Router()

@ustoz_router.message(F.text == "Ustoz kerak")
async def start_ustoz(msg: Message, state: FSMContext):
    data = """Ustoz topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
    await msg.answer(data)
    await msg.answer("Ism, familiyangizni kiriting?")
    await state.set_state(UstozState.ism_familiya)

@ustoz_router.message(UstozState.ism_familiya)
async def get_age(msg: Message, state: FSMContext):
    await state.update_data(ism_familiya=msg.text)
    data = """🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19"""
    await msg.answer(data)
    await state.set_state(UstozState.yosh)

@ustoz_router.message(UstozState.yosh)
async def get_texnology(msg: Message, state: FSMContext):
    await state.update_data(yosh=msg.text)
    data = """📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
    await msg.answer(data)
    await state.set_state(UstozState.texnologiya)

@ustoz_router.message(UstozState.texnologiya)
async def get_aloqa(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await msg.answer(data)
    await state.set_state(UstozState.aloqa)

@ustoz_router.message(UstozState.aloqa)
async def get_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await msg.answer(data)
    await state.set_state(UstozState.hudud)

@ustoz_router.message(UstozState.hudud)
async def get_narx(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    data = """💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
    await msg.answer(data)
    await state.set_state(UstozState.narx)

@ustoz_router.message(UstozState.narx)
async def get_kasb(msg: Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    data = """👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
    await msg.answer(data)
    await state.set_state(UstozState.kasb)

@ustoz_router.message(UstozState.kasb)
async def get_murojat(msg: Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    data = """🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
    await msg.answer(data)
    await state.set_state(UstozState.murojat)

@ustoz_router.message(UstozState.murojat)
async def get_maqsad(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    data = """🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering."""
    await msg.answer(data)
    await state.set_state(UstozState.maqsad)

@ustoz_router.message(UstozState.maqsad)
async def get_all(msg: Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    await msg.answer(f"Ustoz kerak:\n"
                     f"\n"
                     f"🎓 Shogird: {data.get('ism_familiya')}\n"
                     f"🌐 Yosh: {data.get('yosh')}\n"
                     f"📚 Texnologiya: {data.get('texnologiya')}\n"
                     f"🇺🇿 Telegram: {data.get(msg.from_user.username)}\n"
                     f"📞 Aloqa: {data.get('aloqa')}\n"
                     f"🌐 Hudud: {data.get('hudud')}\n"
                     f"💰 Narxi: {data.get('narx')}\n"
                     f"👨🏻‍💻 Kasbi: {data.get('kasb')}\n"
                     f"🕰 Murojaat qilish vaqti: {data.get('murojat')}\n"
                     f"🔎 Maqsad: {data.get('maqsad')}")
    data2 = "Barcha ma'lumotlar to'g'rimi?"
    await msg.answer(data2, reply_markup=hayoq)

@ustoz_router.message(F.text == "Ha")
async def send_ha(msg: Message):
    await msg.answer("""📪 So`rovingiz tekshirish uchun adminga jo`natildi!

E'lon 24-48 soat ichida kanalda chiqariladi.""", reply_markup=menu)

@ustoz_router.message(F.text == "Yo'q")
async def send_yoq(msg: Message):
    await msg.answer("Qabul qilinmadi", reply_markup=menu)