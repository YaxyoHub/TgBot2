import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from api_token import API_TOKEN
from default_btn_py import menu
from inline_btn import inline_btn

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    user = message.from_user.first_name
    await message.answer(f"Salom {user}", reply_markup=menu)


@dp.message(Command("Default_button"))
async def start(message: Message):
    await message.answer("Mana", reply_markup=menu)

@dp.message(F.text == "🔙Asosiy menu")
async def start(message: Message):
    await message.answer("Buyurtmani birga joylashtiramizmi?🤗\n"
                         "Quyidagilardan birini tanlang", reply_markup=inline_btn)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot is running...')
    asyncio.run(main())
