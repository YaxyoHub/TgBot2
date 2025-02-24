from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt yuborish", request_contact=True)],
        [KeyboardButton(text="Lokatsiya yuborish", request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)