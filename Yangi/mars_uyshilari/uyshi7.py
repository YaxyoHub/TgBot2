import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


button1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Inline tugma", callback_data="Inline tugma")]
    ]
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Yangiliklar", callback_data="Yangiliklar")],
        [InlineKeyboardButton(text="Aloqa", callback_data="Aloqa")],
    ]
)

ha_yoq = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha", callback_data="Ha"), InlineKeyboardButton(text="Yo'q", callback_data="Yo'q")]
    ]
)

@dp.message(Command('start'))
async def cmd_start(msg: Message):
    await msg.answer('Salom', reply_markup=button1)

@dp.message(F.text == "Inline tugma")
async def a(msg: Message):
    await msg.reply(f"Salom, Bu inline tugma", reply_markup=menu)

@dp.message(F.text == "Yangiliklar")
async def yangiliklar(msg: Message):
    await msg.answer("Bu kunning yangiliklari!\nBu bot sizga yoqdimi?", reply_markup=ha_yoq)

@dp.message(F.text == "Aloqa")
async def aloqa(msg: Message):
    await msg.answer("Biz bilan bog'laning\n(+998) 94 820 05-51\nBu bot sizga yoqdimi?", reply_markup=ha_yoq)

@dp.message(F.text == "Ha")
async def ha(msg: Message):
    await msg.answer("Rahmat!")


@dp.message(F.text == "Yo'q")
async def ha(msg: Message):
    await msg.answer("Xo'p, keyingi safar yaxshiroq bo'lamiz!")




async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot is running...')
    asyncio.run(main())