import types

from aiogram import Router, types, Bot
from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery

import keyboards_start
from keyboards_start import *


router = Router()


@router.message(F.chat.type.in_({"private"}), CommandStart)
async def start( message: types.Message):
    await message.answer("Привіт, я бот твій", reply_markup= start_buttons)

@router.callback_query(F.data == "developers")
async def start_buttons(message: types.Message, callback: CallbackQuery):
    await callback.answer()
    await message.answer("Розробники @Felyaz @kitnapufiku ")