import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.types import (Message, FSInputFile, BotCommand,
                           BotCommandScopeDefault, ReplyKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup, WebAppInfo)
from aiogram.filters import Command
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


menu_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Google", web_app=WebAppInfo(url="https://google.com")),
            KeyboardButton(text="Canva", web_app=WebAppInfo(url="https://canva.com"))
        ],
        [
            KeyboardButton(text="Youtube", web_app=WebAppInfo(url="https://youtube.com")),
            KeyboardButton(text="Instagram login", web_app=WebAppInfo(url="https://instagram.com")),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


lang_btn = ReplyKeyboardMarkup(

    keyboard=[
        [
            KeyboardButton(text="Uzbek"),
            KeyboardButton(text="Rus tili")],
        [
            KeyboardButton(text="English")
        ]

    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


async def menu_button():
    commands = [
        BotCommand(command="start", description="Botni ishga tushurish uchun"),
        BotCommand(command="language", description="Tilni o'zgartirish"),
        BotCommand(command="apps", description="Ilovalar"),
        BotCommand(command="rasm", description="Sizga rasm junatiladi"),
        BotCommand(command="video", description="sizga Video junatiladi"),
        BotCommand(command="document", description="sizga pdf boradi"),

    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

@dp.message(Command("apps"))
async def apps(message: Message):
    await message.answer("Tanlang", reply_markup=menu_btn)

@dp.message(Command("language"))
async def lang(message: Message):
    await message.answer("Tilni tanlang", reply_markup=lang_btn)


@dp.message(Command("start"))
async def a(message: Message):
    user = message.from_user.first_name
    await message.answer(f"Salom {user}\n"
                         f"/rasm\n"
                         f"/video\n"
                         f"/document")

@dp.message(Command("rasm"))
async def return_rasm(message: Message):
    rasm_yunalish = "image/mars.jpg"
    try:
        rasm = FSInputFile(rasm_yunalish)
        await message.answer_photo(rasm)
    except:
        await message.answer("Rasm yo'q")

@dp.message(Command("video"))
async def return_rasm(message: Message):
    video_yunalish = "video/IMG_5085.MP4"
    try:
        video = FSInputFile(video_yunalish)
        await message.answer_video(video)
    except:
        await message.answer("Video yo'q")

@dp.message(Command("document"))
async def return_docs(message: Message):
    doks_yunalish = "docs/aiogram.pdf"
    try:
        docs = FSInputFile(doks_yunalish)
        await message.answer_document(docs)
    except:
        await message.answer("Dokument yo'q")


async def main():
    await menu_button()
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot is running...')
    asyncio.run(main())
