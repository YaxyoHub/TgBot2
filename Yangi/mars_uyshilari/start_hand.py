from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.context import FSMContext
from state.register_state import UserRegister

start_router = Router()

@start_router.message(Command("start"))
async def start_cmd(msg: Message, state: FSMContext):
    await msg.answer("To'liq ismingizni kiriting:")
    await state.set_state(UserRegister.full_name)

@start_router.message(UserRegister.full_name)
async def phone_number(msg: Message, state: FSMContext):
    await state.update_data(full_name=msg.text)
    await msg.answer("Tug'ilgan sanangizni yuboring")
    await state.set_state(UserRegister.birth_date)

@start_router.message(UserRegister.birth_date)
async def full_name(msg: Message, state: FSMContext):
    await state.update_data(birth_date=msg.text)
    await msg.answer("Telefon raqamingizni yuboring")
    await state.set_state(UserRegister.phone_number)

@start_router.message(UserRegister.phone_number)
async def phone_number(msg: Message, state: FSMContext):
    await state.update_data(phone_number=msg.text)
    await msg.answer("Emailingizni yuboring")
    await state.set_state(UserRegister.email)

@start_router.message(UserRegister.email)
async def username(msg: Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer("Username ingizni yuboring")
    await state.set_state(UserRegister.username)

@start_router.message(UserRegister.username)
async def password(msg: Message, state: FSMContext):
    await state.update_data(username=msg.text)
    await msg.answer("Ishonchli parol yuboring")
    await state.set_state(UserRegister.password)

@start_router.message(UserRegister.password)
async def avatar(msg: Message, state: FSMContext):
    await state.update_data(password=msg.text)
    data = await state.get_data()
    await msg.answer(f"Ism-Familiya: {data.get('full_name')}\n"
                     f"Tug'ilgan sana: {data.get('birth_date')}\n"
                     f"Telefo raqam: {data.get('phone_number')}\n"
                     f"Email: {data.get('email')}\n"
                     f"Username: {data.get('username')}\n"
                     f"Parol: {data.get('password')}\n")
    await state.clear()