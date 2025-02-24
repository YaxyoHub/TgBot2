from aiogram.fsm.state import State, StatesGroup

class UserRegister(StatesGroup):
    full_name = State()
    birth_date = State()
    phone_number = State()
    email = State()
    username = State()
    password = State()