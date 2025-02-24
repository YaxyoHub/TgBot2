import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_TOKEN
from aiogram.filters import Command
import wikipedia


bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# Start komandasi uchun handler
@dp.message(Command('start'))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🇬🇧 English", callback_data='lang_en'))
    keyboard.add(InlineKeyboardButton("🇺🇿 O'zbekcha", callback_data='lang_uz'))
    keyboard.add(InlineKeyboardButton("🇷🇺 Русский", callback_data='lang_ru'))

    await message.answer("Ma'lumotlar qaysi tilda chiqarilsin? Quyidagi tillardan birini tanlang:",
                         reply_markup=keyboard)


# Til tanlanganda ishlaydigan callback
@dp.callback_query_handler(lambda c: c.data.startswith('lang_'))
async def process_language(callback_query: types.CallbackQuery):
    lang = callback_query.data.split('_')[1]
    wikipedia.set_lang(lang)
    await bot.send_message(callback_query.from_user.id, "Sizga qaysi mavzu bo'yicha ma'lumot kerak?")




# Mavzu bo'yicha ma'lumot olish
@dp.message()
async def get_wikipedia_info(message: types.Message)
    lang = ""
    wikipedia.set_lang(lang)
    try:
        summary = wikipedia.summary(message.text, sentences=3)
        await message.answer(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"Ko'p ma'lumot topildi, aniqroq yozing: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await message.answer("Bu mavzu bo'yicha hech narsa topilmadi.")


if __name__ == "__main__":
    dp.start_polling( skip_updates=True)