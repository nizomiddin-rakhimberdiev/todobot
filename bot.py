from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from keyboards import menu, done, delete
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
    await message.answer(f"Assalamu alaykum, {message.from_user.full_name}\n", reply_markup=menu)


@dp.message_handler(text="Tasklar ro'yxati")
async def todos(message: types.Message):
    todos = db.get_todos()
    print(todos)
    for todo in todos:
        text = ""
        text += f"ID: {todo[0]}\n"
        text += f"Title: {todo[1]}\n"
        text += f"Description: {todo[2]}\n"
        if todo[3] == 0:
            text += f"Status: Bajarilmagan\n"
        elif todo[3] == 1:
            text += f"Status: Bajarilgan ✅\n"
        text += f"Sana: {todo[4]}\n"

        if todo[3] == 0:
            await message.answer(text, reply_markup=done)
        elif todo[3] == 1:
            await message.answer(text, reply_markup=delete)


@dp.message_handler(text="Yangi task yaratish")
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


@dp.callback_query_handler(text='bajarildi')
async def update_status(call: types.CallbackQuery):
    text = call.message.text
    id = text.split('\n')[0]
    id = id[4:]
    print(type(id))
    print(id)
    db.update_todo(id)
    await call.message.answer("Status o'zgartirildi")


@dp.callback_query_handler(text='delete')
async def update_status(call: types.CallbackQuery):
    text = call.message.text
    id = text.split('\n')[0]
    id = id[4:]
    print(type(id))
    print(id)
    db.delete_todo(id)
    await call.message.answer("Todo o'chirildi")
    # bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
