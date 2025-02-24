import asyncio

from aiogram import Bot, Dispatcher

from data.config import API_TOKEN

from handlers.start_hand import start_router
from handlers.sherik_hand import sherik_router
from handlers.ish_hand import ish_router
from handlers.hodim_hand import hodim_router
from handlers.ustoz_hand import ustoz_router
from handlers.shogird_hand import shogird_router


bot = Bot(token=API_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(sherik_router)
dp.include_router(ish_router)
dp.include_router(hodim_router)
dp.include_router(ustoz_router)
dp.include_router(shogird_router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Bot ishga tushdi...")
    asyncio.run(main())



