from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔙Asosiy menu")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Tanlang..."
)
