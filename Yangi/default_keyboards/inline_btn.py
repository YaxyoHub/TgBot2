from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛒Buyurtma berish", callback_data='Buyurtma bering')],
        [InlineKeyboardButton(text="ℹ️Biz haqimizda", callback_data="Biz haqimizda"), InlineKeyboardButton(text="🛍Buyurtmalarim", callback_data="Buyurtmalarim")],
        [InlineKeyboardButton(text="🏘Filiallar", callback_data='Filiallar')],
        [InlineKeyboardButton(text="✍️Fikr bildirish", callback_data='Fikr bildirish'), InlineKeyboardButton(text="⚙️Sozlamalar", callback_data='Sozlamalar')],

    ]
)
