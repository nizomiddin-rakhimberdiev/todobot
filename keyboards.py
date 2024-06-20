from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btns = [KeyboardButton("Tasklar ro'yxati"), KeyboardButton("Yangi task yaratish")]
menu.add(*btns)


done = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Bajarildi ✅", callback_data="bajarildi"),
            InlineKeyboardButton("Delete ❌", callback_data="delete"),
        ]
    ]
)

delete = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("Delete ❌", callback_data="delete"),
        ]
    ]
)