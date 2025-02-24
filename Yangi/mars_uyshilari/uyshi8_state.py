import asyncio

from aiogram import Bot, Dispatcher
from mars_uyshilari.config import API_TOKEN
from mars_uyshilari.start_hand import start_router

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('Bot is running...')
    asyncio.run(main())