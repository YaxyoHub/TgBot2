from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ustoz_shogird.buttons.default import hayoq, menu

from ustoz_shogird.states.state_menu import IshState

ish_router = Router()

@ish_router.message(F.text == "Ish joyi kerak")
async def start_ish(msg: Message, state: FSMContext):
    data = """Ish joyi topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.\n
Ism, familiyangizni kiriting?"""
    await msg.answer(data)
    await state.set_state(IshState.ism_familiya)

@ish_router.message(IshState.ism_familiya)
async def get_age(msg: Message, state: FSMContext):
    await state.update_data(ism_familiya=msg.text)
    data = """🕑 Yosh: 

Yoshingizni kiriting?
Masalan, 19"""
    await msg.answer(data)
    await state.set_state(IshState.yosh)

@ish_router.message(IshState.yosh)
async def get_texnology(msg: Message, state: FSMContext):
    await state.update_data(yosh=msg.text)
    data = """📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
    await msg.answer(data)
    await state.set_state(IshState.texnologiya)

@ish_router.message(IshState.texnologiya)
async def get_aloqa(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await msg.answer(data)
    await state.set_state(IshState.aloqa)

@ish_router.message(IshState.aloqa)
async def get_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await msg.answer(data)
    await state.set_state(IshState.hudud)

@ish_router.message(IshState.hudud)
async def get_narx(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    data = """💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
    await msg.answer(data)
    await state.set_state(IshState.narx)

@ish_router.message(IshState.narx)
async def get_kasb(msg: Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    data = """👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
    await msg.answer(data)
    await state.set_state(IshState.kasb)

@ish_router.message(IshState.kasb)
async def get_murojat(msg: Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    data = """🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
    await msg.answer(data)
    await state.set_state(IshState.murojat)

@ish_router.message(IshState.murojat)
async def get_maqsad(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    data = """🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering."""
    await msg.answer(data)
    await state.set_state(IshState.maqsad)

@ish_router.message(IshState.maqsad)
async def get_all(msg: Message, state: FSMContext):
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    await msg.answer(f"Ish joyi kerak:\n"
                     f"\n"
                     f"👨‍💼 Xodim: {data.get('ism_familiya')}\n"
                     f"🕑 Yosh: {data.get('yosh')}\n"
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

@ish_router.message(F.text == "Ha")
async def send_ha(msg: Message):
    await msg.answer("""📪 So`rovingiz tekshirish uchun adminga jo`natildi!

E'lon 24-48 soat ichida kanalda chiqariladi.""", reply_markup=menu)

@ish_router.message(F.text == "Yo'q")
async def send_yoq(msg: Message):
    await msg.answer("Qabul qilinmadi", reply_markup=menu)
