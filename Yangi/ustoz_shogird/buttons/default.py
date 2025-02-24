from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustoz kerak")],
        [KeyboardButton(text="Shogird kerak")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Buttonlardan birini tanlang",
    one_time_keyboard=True
)

hayoq = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Ha"), KeyboardButton(text="Yo'q")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)