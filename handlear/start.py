from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold


router_start = Router()


@router_start.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
   await message.answer("add_note - добавить заметку и выбрать время для напаминания"
                        "\n"
                        "delete_note - удалить заметку"
                        "\n"
                        "all_note - посмотреть все заметки "






                        )