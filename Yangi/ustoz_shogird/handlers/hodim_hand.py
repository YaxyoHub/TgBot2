from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from ustoz_shogird.buttons.default import hayoq, menu

from ustoz_shogird.states.state_menu import XodimState

hodim_router = Router()

@hodim_router.message(F.text == "Hodim kerak")
async def start_hodim(msg: Message, state: FSMContext):
    data = """Xodim topish uchun ariza berish

Hozir sizga birnecha savollar beriladi. 
Har biriga javob bering. 
Oxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi."""
    await msg.answer(data)
    await msg.answer("🎓 Idora nomi?")
    await state.set_state(XodimState.idora)

@hodim_router.message(XodimState.idora)
async def get_texnologiya(msg: Message, state: FSMContext):
    await state.update_data(idora=msg.text)
    data = """📚 Texnologiya:

Talab qilinadigan texnologiyalarni kiriting?
Texnologiya nomlarini vergul bilan ajrating. Masalan, 

Java, C++, C#"""
    await msg.answer(data)
    await state.set_state(XodimState.texnologiya)

@hodim_router.message(XodimState.texnologiya)
async def get_aloqa(msg: Message, state: FSMContext):
    await state.update_data(texnologiya=msg.text)
    data = """📞 Aloqa: 

Bog`lanish uchun raqamingizni kiriting?
Masalan, +998 90 123 45 67"""
    await msg.answer(data)
    await state.set_state(XodimState.aloqa)

@hodim_router.message(XodimState.aloqa)
async def det_hudud(msg: Message, state: FSMContext):
    await state.update_data(aloqa=msg.text)
    data = """🌐 Hudud: 

Qaysi hududdansiz?
Viloyat nomi, Toshkent shahar yoki Respublikani kiriting."""
    await msg.answer(data)
    await state.set_state(XodimState.hudud)

@hodim_router.message(XodimState.hudud)
async def get_masul(msg: Message, state: FSMContext):
    await state.update_data(hudud=msg.text)
    await msg.answer("✍️Mas'ul ism sharifi?")
    await state.set_state(XodimState.masul)

@hodim_router.message(XodimState.masul)
async def get_murojat(msg: Message, state: FSMContext):
    await state.update_data(masul=msg.text)
    data = """🕰 Murojaat qilish vaqti: 

Qaysi vaqtda murojaat qilish mumkin?
Masalan, 9:00 - 18:00"""
    await msg.answer(data)
    await state.set_state(XodimState.murojat)

@hodim_router.message(XodimState.murojat)
async def get_vaqt(msg: Message, state: FSMContext):
    await state.update_data(murojat=msg.text)
    await msg.answer("🕰 Ish vaqtini kiriting?")
    await state.set_state(XodimState.vaqt)

@hodim_router.message(XodimState.vaqt)
async def get_maosh(msg: Message, state: FSMContext):
    await state.update_data(vaqt=msg.text)
    await msg.answer("💰 Maoshni kiriting?")
    await state.set_state(XodimState.maosh)

@hodim_router.message(XodimState.maosh)
async def get_qushimcha(msg: Message, state: FSMContext):
    await state.update_data(maosh=msg.text)
    await msg.answer("‼️ Qo`shimcha ma`lumotlar?")
    await state.set_state(XodimState.qushimcha)

@hodim_router.message(XodimState.qushimcha)
async def get_all(msg: Message, state: FSMContext):
    await state.update_data(qushimcha=msg.text)
    data = await state.get_data()
    await msg.answer(f"Xodim kerak:\n"
                     f"\n"
                     f"🏢 Idora: {data.get('idora')}\n"
                     f"📚 Texnologiya: {data.get('texnologiya')}\n"
                     f"🇺🇿 Telegram: {msg.from_user.username}\n"
                     f"📞 Aloqa: {data.get('aloqa')}\n"
                     f"🌐 Hudud: {data.get('hudud')}\n"
                     f"✍️ Mas'ul: {data.get('masul')}\n"
                     f"🕰 Murojaat vaqti: {data.get('murojat')}\n"
                     f"🕰 Ish vaqti: {data.get('vaqt')}\n"
                     f"💰 Maosh: {data.get('maosh')}\n"
                     f"‼️ Qo`shimcha: {data.get('qushimcha')}")
    data2 = "Barcha ma'lumotlar to'g'rimi?"
    await msg.answer(data2, reply_markup=hayoq)

@hodim_router.message(F.text == "Ha")
async def send_ha(msg: Message):
    await msg.answer("""📪 So`rovingiz tekshirish uchun adminga jo`natildi!

E'lon 24-48 soat ichida kanalda chiqariladi.""", reply_markup=menu)

@hodim_router.message(F.text == "Yo'q")
async def send_yoq(msg: Message):
    await msg.answer("Qabul qilinmadi", reply_markup=menu)