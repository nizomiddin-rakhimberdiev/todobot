from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from database import Database

TOKEN = "7008107531:AAEZTtYqdw9MZD8yXy094CcggeyEOhjoqWo"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()

import os
import django

# Django settings faylini ko'rsatamiz

class TodoState(StatesGroup):
    title = State()
    description = State()


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"Assalamu alaykum, {message.from_user.full_name}\n"
                         f"Tasklar ro'yxatini ko'rish uchun /todos ni bosing\n"
                         f"Agar Task yaratmochi bo'lsangiz /create_todo ni bosing")


@dp.message_handler(commands=["todos"])
async def todos(message: types.Message):
    todos = db.get_todos()
    for todo in todos:
        text = ""
        for i in todo:
            text += str(i) + "\n"

        await message.answer(text)

@dp.message_handler(commands=["create_todo"])
async def create_todo(message: types.Message):
    await message.answer("Titleni kiriting:")
    await TodoState.title.set()

@dp.message_handler(state=TodoState.title)
async def create_todo(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer("Descriptionni kiriting: ")
    await TodoState.description.set()

@dp.message_handler(state=TodoState.description)
async def create_todo(message: types.Message, state: FSMContext):
    await state.update_data(description=message.text)
    data = await state.get_data()
    title = data.get("title")
    description = data.get("description")

    db.add_todo(title, description)
    await state.finish()
    await message.answer("Todo yaratildi. Todo listni ko'rish uchun /todos ni bosing")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
