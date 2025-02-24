import asyncio

from aiogram import Bot, Dispatcher
from data.apitoken import API_TOKEN
from handlers.msg_return import message
from dars_3.data.apitoken import PAY

bot = Bot(token=API_TOKEN)
dp = Dispatcher()





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot is running...')
    asyncio.run(main())