import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from aiogram.filters import Command
from config import API_TOKEN
from oqtepalavash.buttons import lang_menu, menu, asosiy_menu, eats_menu

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(msg: Message):
    user = msg.from_user.first_name
    await msg.answer(f"Salom {user}", reply_markup=lang_menu)


@dp.message(F.text == "🇺🇿O'zbek tili")
async def uzb(msg: Message):
    await msg.answer("Siz O'zbek tilini tanladingiz", reply_markup=menu)


@dp.message(F.text.in_(["🇷🇺Русский язык", "🇬🇧English"]))
async def rus(msg: Message):
    await msg.answer("Afsus hozircha botda 🇷🇺Русский язык va 🇬🇧English ishlamaydi", reply_markup=menu)


@dp.message(F.text == "Asosiy menu")
async def asosiy_menu_func(msg: Message):
    await msg.answer("Marhamat", reply_markup=asosiy_menu)


@dp.message(F.text == "Tillar")
async def tillar_func(msg: Message):
    await msg.answer("Tillar bo'limi", reply_markup=lang_menu)

@dp.callback_query()
async def callback_handlar(callback: types.CallbackQuery):
    if callback.data == "buyurtma":
        await callback.message.answer("***Marhamat menu***\n"
                    "1- 🍔OqTepa Hamburger\n"
                    "💰17900 UZS\n"
                    "2- 🍕OqTepa Pizza\n"
                    "💰68600 UZS\n"
                    "3- 🫔OqTepa Lavash\n"
                    "💰31500 UZS\n"
                    "4- 🌯OqTepa Huggy\n"
                    "💰37500 UZS\n"
                    "5- 🥪OqTepa Sandwich\n"
                    "💰15000 UZS\n"
                    "6- 🍟OqTepa Kartoshka Fri\n"
                    "💰25000 UZS\n"
                    "7- 🥤OqTepa Coca-Cola\n"
                    "💰8000 UZS", reply_markup=eats_menu)


@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "bir":
        await callback.message.answer("🍔OqTepa Hamburger\n"
                                      "Manzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                      "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin", reply_markup=asosiy_menu)
"""----------------------------------------"""
@dp.callback_query()
async def buyurtma(msg: types.CallbackQuery):
    if msg.data == "ikki":
        await msg.message.answer("🍕OqTepa Pizza\nManzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                 "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin")
"""----------------------------------------"""
@dp.callback_query()
async def buyurtma(msg: types.CallbackQuery):
    if msg.data == "uch":
        await msg.message.answer("🫔OqTepa Lavash\nManzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                 "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin")
"""-----------------------------------------"""
@dp.callback_query()
async def buyurtma(msg: types.CallbackQuery):
    if msg.data == "tort":
        await msg.message.answer("🌯OqTepa Huggy\nManzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                 "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin")
"""---------------------------------------------"""
@dp.callback_query()
async def buyurtma(msg: types.CallbackQuery):
    if msg.data == "besh":
        await msg.message.answer("🥪OqTepa Sandwich\nManzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                 "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin")
"""-----------------------------------------------"""
@dp.callback_query()
async def buyurtma(msg: types.CallbackQuery):
    if msg.data == "olti":
        await msg.message.answer("🍟OqTepa Kartoshka Fri\nManzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                 "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin")
"""------------------------------------------------"""
@dp.callback_query()
async def buyurtma(msg: types.CallbackQuery):
    if msg.data == "yetti":
        await msg.message.answer("🥤OqTepa Coca-Cola\nManzilingizni qoldiring va buyurtmani qabul qilib oling\n"
                                 "To'lovni buyurtmani qabul qilganingizdan so'ng qilishingiz mumkin")
"""------------------------------------------------"""
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "biz":
        await callback.message.answer("OqTepaLavash\n📍Angren shahri\n📞(+998) 94 820 05-51", reply_markup=asosiy_menu)
"""------------------------------------------------"""
@dp.callback_query()
async def buyurtmalarim_func(msg: types.CallbackQuery):
    if msg.data == "buyurtma2":
        await msg.message.answer("Hozircha buyutmalar tarixi bo'sh")
"""-------------------------------------------------------------"""
@dp.callback_query()
async def filial(callback: types.CallbackQuery):
    if callback.data == "filial":
        await callback.message.answer("1-Angren filiali\n2-Toshkent filiali\n3-Qo'qon filiali")

async def main():
    print("Bot ishlayapti...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
