import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

TOKEN = "8116460300:AAFfl3gbso3YUwhOUB5U5xFuthxxHfN8d0M"

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())