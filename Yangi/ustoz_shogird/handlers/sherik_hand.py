from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ustoz_shogird.buttons.default import hayoq, menu


from ustoz_shogird.states.state_menu import SherikState

sherik_router = Router()


@sherik_router.message(F.text == "Sherik kerak")
async def start_sherik(msg: Message, state: FSMContext):
    await msg.answer("Ism, familiyangizni kiriting?")
    await state.set_state(SherikState.ism_familiya)

@sherik_router.message(SherikState.ism_familiya)
async def get_name(msg: Message, state: FSMContext):
    await state.update_data(ism_familiya=msg.text)
    data = """
📚 Texnologiya:
Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 
Java, C++, C#
"""
    await msg.answer(data)
    await state.set_state(SherikState.texnologiya)

@sherik_router.message(SherikState.texnologiya)
async def get_aloqa(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await msg.answer(data)
    await state.set_state(SherikState.aloqa)

@sherik_router.message(SherikState.aloqa)
async def get_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await msg.answer(data)
    await state.set_state(SherikState.hudud)

@sherik_router.message(SherikState.hudud)
async def get_narx(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    data = """💰 Narxi:

Tolov qilasizmi yoki Tekinmi?
Kerak bo`lsa, Summani kiriting?"""
    await msg.answer(data)
    await state.set_state(SherikState.narx)

@sherik_router.message(SherikState.narx)
async def get_kasb(msg: Message, state: FSMContext):
    await state.update_data(narx=msg.text)
    data = """👨🏻‍💻 Kasbi: 

Ishlaysizmi yoki o`qiysizmi?
Masalan, Talaba"""
    await msg.answer(data)
    await state.set_state(SherikState.kasb)

@sherik_router.message(SherikState.kasb)
async def get_murojat(msg: Message, state: FSMContext):
    await state.update_data(kasb=msg.text)
    data = """🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
    await msg.answer(data)
    await state.set_state(SherikState.murojat)

@sherik_router.message(SherikState.murojat)
async def get_maqsad(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    data = """🔎 Maqsad: 

Maqsadingizni qisqacha yozib bering."""
    await msg.answer(data)
    await state.set_state(SherikState.maqsad)

@sherik_router.message(SherikState.maqsad)
async def get_tekshir(msg: Message, state: FSMContext):
    user = msg.from_user.username
    await state.update_data(maqsad=msg.text)
    data = await state.get_data()
    await msg.answer(f"Sherik kerak:   \n\n"
                     f"🏅 Sherik: {data.get('ism_familiya')}\n"
                     f"📚 Texnologiya: {data.get('texnologiya')}\n"
                     f"🇺🇿 Telegram: @{user}\n"
                     f"📞 Aloqa: {data.get('aloqa')}\n"
                     f"🌐 Hudud: {data.get('hudud')}\n"
                     f"💰 Narxi: {data.get('narx')}\n"
                     f"👨🏻‍💻 Kasbi: {data.get('kasb')}\n"
                     f"🕰 Murojaat qilish vaqti: {data.get('murojat')}\n"
                     f"🔎 Maqsad: {data.get('maqsad')}\n")
    data2 = "Barcha ma'lumotlar to'g'rimi?"
    await msg.answer(data2 ,reply_markup=hayoq)

@sherik_router.message(F.text == "Ha")
async def send_ha(msg: Message):
    await msg.answer("""📪 So`rovingiz tekshirish uchun adminga jo`natildi!

E'lon 24-48 soat ichida kanalda chiqariladi.""", reply_markup=menu)

@sherik_router.message(F.text == "Yo'q")
async def send_yoq(msg: Message):
    await msg.answer('Qabul qilinmadi', reply_markup=menu)


