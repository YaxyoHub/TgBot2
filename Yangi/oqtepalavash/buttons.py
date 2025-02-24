from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,
                           InlineKeyboardMarkup)


lang_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿O'zbek tili"), KeyboardButton(text="🇷🇺Русский язык")],
        [KeyboardButton(text="🇬🇧English")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Til tanlang",
    one_time_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Asosiy menu"), KeyboardButton(text="Tillar")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Tanlang"
)

asosiy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🛒Buyurtma berish", callback_data='buyurtma')],
        [InlineKeyboardButton(text="ℹ️Biz haqimizda", callback_data="biz"), InlineKeyboardButton(text="🛍Buyurtmalarim", callback_data="buyurtma2")],
        [InlineKeyboardButton(text="🏘Filiallar", callback_data='filial')]
    ]
)

eats_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="bir"), InlineKeyboardButton(text="2", callback_data="ikki"), InlineKeyboardButton(text="3", callback_data="uch"), InlineKeyboardButton(text="4", callback_data="tort")],
        [InlineKeyboardButton(text="5", callback_data="besh"), InlineKeyboardButton(text="6", callback_data="olti"), InlineKeyboardButton(text="7", callback_data="yetti")]
    ]
)