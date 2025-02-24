from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiohttp import request

cars = {
    "BMW M5": { "model": "M5", "year": 2023, "color": "Kulrang", "hp": 600, "maxSpeed": "305 km/h", "image": "image/bmw.jpg" },
    "Mercedes-AMG G63": { "model": "G63", "year": 2022, "color": "Qora", "hp": 577, "maxSpeed": "220 km/h", "image": "image/mercedes.jpg" },
    "Audi RS7": { "model": "RS7", "year": 2023, "color": "Qizil", "hp": 591, "maxSpeed": "305 km/h", "image": "image/audi.jpg" },
    "Porsche 911 Turbo S": { "model": "911 Turbo S", "year": 2023, "color": "Qizil", "hp": 640, "maxSpeed": "330 km/h", "image": "image/porsche.jpg" },
    "Tesla Model S Plaid": { "model": "Model S Plaid", "year": 2023, "color": "Qizil", "hp": 1020, "maxSpeed": "322 km/h", "image": "image/tesla.jpg" },
    "Lamborghini Urus": { "model": "Urus", "year": 2023, "color": "Sariq", "hp": 657, "maxSpeed": "305 km/h", "image": "image/lamborgini.jpg" },
    "Ferrari SF90": { "model": "SF90 Stradale", "year": 2023, "color": "Qizil", "hp": 986, "maxSpeed": "340 km/h", "image": "image/ferrari.jpg" },
    "Bugatti Chiron": { "model": "Chiron", "year": 2023, "color": "Sariq", "hp": 1500, "maxSpeed": "420 km/h", "image": "image/bugatti.jpg" },
    "Rolls-Royce Ghost": { "model": "Ghost", "year": 2023, "color": "", "hp": 563, "maxSpeed": "250 km/h", "image": "image/rolls_royce.jpg" },
    "McLaren 720S": { "model": "720S", "year": 2023, "color": "Oq", "hp": 710, "maxSpeed": "341 km/h", "image": "image/mclaren.jpg" }
}

car_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="BMW M5"), KeyboardButton(text="Mercedes-AMG G63")],
        [KeyboardButton(text="Audi RS7"), KeyboardButton(text="Porsche 911 Turbo S  ")],
        [KeyboardButton(text="Tesla Model S Plaid"), KeyboardButton(text="Lamborghini Urus")],
        [KeyboardButton(text="Ferrari SF90"), KeyboardButton(text="Bugatti Chiron")],
        [KeyboardButton(text="Rolls-Royce Ghost"), KeyboardButton(text="McLaren 720S")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Quyidagilardan biron avtomobilni tanlang..."
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Kontakt yuborish", request_contact=True)],
        [KeyboardButton(text="Lokatsiya yuborish", request_location=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

lang_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇺🇿 O'zbekcha"), KeyboardButton(text="🇬🇧 English")],
        [KeyboardButton(text="🇷🇺 Русский")]
    ]
)
