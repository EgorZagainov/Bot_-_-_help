from datetime import datetime

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

router_sqlite3 = Router()


import sqlite3


db = sqlite3.connect('db3')
cursor = db.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        chat_id INTEGER,
        username TEXT,
        full_name TEXT,
        last_command_time TEXT
    )
''')

db.commit()

@router_sqlite3.message(Command('start_sqlite3'))
async def command_start_handler(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.from_user.username
    full_name = message.from_user.full_name

    cursor.execute('''
            INSERT INTO users (user_id, chat_id, username, full_name) VALUES (?, ?, ?, ?)
        ''', (user_id, chat_id, username, full_name))

    db.commit()

    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    await message.answer("Привет, для выбора товара или услуги запусти команду:\n"
                         "\n"
                         "/robot")


# Обработчик команды /add_time
@router_sqlite3.message(Command('add_time'))
async def cmd_add_time(message: Message):
    user_id = message.chat.id
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute('''
        UPDATE users SET last_command_time = ? WHERE user_id = ?
    ''', (current_time, user_id))

    db.commit()

    await message.answer(f'Время добавления: {current_time}')


# Обработчик команды /get_data
@router_sqlite3.message(Command('get_data'))
async def cmd_get_data(message: Message):
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()

    for user_data in users_data:
        await message.answer(f"User ID: {user_data[1]}, Chat ID: {user_data[2]}, "
                             f"Username: {user_data[3]}, Full Name: {user_data[4]}, "
                             f"Last Command Time: {user_data[5]}")

# Обработчик команды /delete_user
@router_sqlite3.message(Command('delete_user'))
async def cmd_delete_user(message: Message):
    user_id = message.chat.id

    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    db.commit()

    await message.answer("Ваши данные были удалены из базы данных.")