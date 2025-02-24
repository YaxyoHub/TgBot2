from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

message = Router()

@message.message()
async def a(msg: Message):
    user_text = msg.text
    await msg.reply(user_text)
