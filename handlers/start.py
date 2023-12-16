import os
from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardMarkup

from loader import bot

router_start = Router()





@router_start.message(CommandStart())
async def cmd_start(message: types.Message) -> None:

   await message.answer("/add_note - добавить заметку и выбрать время для напоминания"
                        "\n"
                        "/delete_note - удалить заметку"
                        "\n"
                        "/all_note - посмотреть все заметки ")


