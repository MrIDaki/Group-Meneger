import types

from aiogram import Router
from aiogram import F
from aiogram.filters import CommandStart

from main import *

router = Router()


@router.message(F.chat.type.in_({"private"}),CommandStart)
async def start(bot:Bot, message: types.Message):
    await bot.send_message("Привіт, я бот твій", reply_to_message_id=message.message_id)
