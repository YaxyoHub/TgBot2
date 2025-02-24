from aiogram.fsm.state import State, StatesGroup


class SherikState(StatesGroup):
    ism_familiya = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    murojat = State()
    maqsad = State()
    tekshir = State()

class IshState(StatesGroup):
    ism_familiya = State()
    yosh = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    murojat = State()
    maqsad = State()

class XodimState(StatesGroup):
    idora = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    masul = State()
    murojat = State()
    vaqt = State()
    maosh = State()
    qushimcha = State()

class ShogirdState(StatesGroup):
    ism_familiya = State()
    yosh = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    murojat = State()
    maqsad = State()

class UstozState(StatesGroup):
    ism_familiya = State()
    yosh = State()
    texnologiya = State()
    aloqa = State()
    hudud = State()
    narx = State()
    kasb = State()
    murojat = State()
    maqsad = State()
