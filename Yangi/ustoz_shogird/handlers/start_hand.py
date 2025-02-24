from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from buttons.default import menu

start_router = Router()

@start_router.message(Command("start"))
async def start_cmd(msg: Message):
    data = f"""Assalom alaykum {msg.from_user.first_name}
UstozShogird kanalining rasmiy botiga xush kelibsiz!
/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!"""
    await msg.answer(data, reply_markup=menu)


@start_router.message(Command("help"))
async def help_cmd(msg: Message):
    data = """UzGeeks faollari tomonidan tuzilgan Ustoz-Shogird kanali. 
Bu yerda Programmalash bo`yicha
  #Ustoz,  
  #Shogird,
  #oquvKursi,
  #Sherik,  
  #Xodim va 
  #IshJoyi 
 topishingiz mumkin. 
E'lon berish: @UstozShogirdBot
Admin @UstozShogirdAdminBot"""
    await msg.answer(data)