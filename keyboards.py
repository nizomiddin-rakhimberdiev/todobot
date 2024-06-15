from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
btns = [KeyboardButton("Tasklar ro'yxati"), KeyboardButton("Yangi task yaratish")]
menu.add(*btns)