from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_buttons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Хто розробник", callback_data="developers")],
    [InlineKeyboardButton(text="Додати бота в чат", url="https://t.me/Test378632_bot?startgroup=true&admin=change_info+delete_messages+invite_users+pin_messages+promote_members")],
    [InlineKeyboardButton(text="Донат на ЗСУ", url="https://savelife.in.ua/donate/#donate-army-card-once") ],
])
