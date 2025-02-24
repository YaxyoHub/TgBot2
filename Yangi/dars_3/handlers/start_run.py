from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext
from dars_3.buttons.default import menu

from state.register_state import UserRegister

start_router = Router()

@start_router.message(Command("start"))
async def start_cmd(msg: Message, state: FSMContext):
    await msg.answer("Iltimos ismingizni kiriting: ")
    await state.set_state(UserRegister.first_name)

@start_router.message(UserRegister.first_name)
async def first_name(msg: Message, state: FSMContext):
    await state.update_data(first_name=msg.text)
    await msg.answer("Familiyangizni kiriting: ")
    await state.set_state(UserRegister.last_name)


@start_router.message(UserRegister.last_name)
async def last_name(msg: Message, state: FSMContext):
    await state.update_data(last_name=msg.text)
    await msg.answer("Yoshingizni kiriting: ")
    await state.set_state(UserRegister.age)


@start_router.message(UserRegister.age)
async def age(msg: Message, state: FSMContext):
    await state.update_data(age=msg.text)
    await msg.answer("Emailingizni kiriting: ")
    await state.set_state(UserRegister.email)


@start_router.message(UserRegister.email)
async def email(msg: Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer("Telefon kiriting: ", reply_markup=menu)
    await state.set_state(UserRegister.phone_number)


@start_router.message(UserRegister.phone_number)
async def phone_number(msg: Message, state: FSMContext):
    await state.update_data(phone_number=msg.text)
    await msg.answer(f"Ism: {state.get_value}\n"
                     f"Familiya: {UserRegister.last_name}\n"
                     f"Yosh: {UserRegister.age}\n"
                     f"Email: {UserRegister.email}\n"
                     f"Raqam: {UserRegister.phone_number}\n"
                     f"Lokatsiya: {UserRegister.location}")

