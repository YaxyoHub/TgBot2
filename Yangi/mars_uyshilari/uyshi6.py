import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from config import API_TOKEN
from menu_button import car_menu

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    user = message.from_user.first_name
    await message.reply(f"Salom {user}", reply_markup=car_menu)


@dp.message(F.text == "BMW M5")
async def bmw(msg: Message):
    rasm_yunalish = "image/bmw.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: M5\nYear: 2023\nColor: Kulrang\nHP: 600\nMaxSpeed: 305 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""-------------------------------------------"""
@dp.message(F.text == "Mercedes-AMG G63")
async def merc(msg: Message):
    rasm_yunalish = "image/mercedes.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: G63n\nYear: 2022\nColor: Qora\nHP: 577\nMaxSpeed: 220 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""-------------------------------------------"""
@dp.message(F.text == "Audi RS7")
async def audi(msg: Message):
    rasm_yunalish = "image/audi.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: RS7\nYear: 2023\nColor: Qizil\nHP: 591\nMaxSpeed: 305 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""-------------------------------------------"""
@dp.message(F.text == "Porsche 911 Turbo S")
async def porsche(msg: Message):
    rasm_yunalish = "image/porsche.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: 911 Turbo S\nYear: 2023\nColor: Qizil\nHP: 640\nmaxSpeed: 330 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""------------------------------------------"""
@dp.message(F.text == "Tesla Model S Plaid")
async def tesla(msg: Message):
    rasm_yunalish = "image/tesla.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: Model S Plaid\nYear: 2023\nColor: Qizil\nHP: 1020\nmaxSpeed: 322 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""------------------------------------------"""
@dp.message(F.text == "Lamborghini Urus")
async def lamborghini(msg: Message):
    rasm_yunalish = "image/lamborgini.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: Urus\nYear: 2023\nColor: Sariq\nHP: 657\nmaxSpeed: 305 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""------------------------------------------"""
@dp.message(F.text == "Ferrari SF90")
async def ferrari(msg: Message):
    rasm_yunalish = "image/ferrari.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: SF90 Stradale\nYear: 2023\nColor: Qizil\nHP: 986\nMaxSpeed: 340 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""------------------------------------------"""
@dp.message(F.text == "Bugatti Chiron")
async def bugatti(msg: Message):
    rasm_yunalish = "image/bugatti.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: Chiron\nYear: 2023\nColor: Sariq\nHP: 1500\nMaxSpeed: 420 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""------------------------------------------"""
@dp.message(F.text == "Rolls-Royce Ghost")
async def rolls(msg: Message):
    rasm_yunalish = "image/rolls_royce.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: Ghost\nYear: 2023\nColor: Oq\nHP: 563\nMaxSpeed: 250 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")
"""------------------------------------------"""
@dp.message(F.text == "McLaren 720S")
async def mclaren(msg: Message):
    rasm_yunalish = "image/mclaren.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await msg.reply(f"Model: 720S\nYear: 2023\nColor: Oq\nHP: 710\nMaxSpeed: 341 km/h")
        await msg.answer_photo(rasm)
    except:
        await msg.answer("Rasm yo'q")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot is running...')
    asyncio.run(main())