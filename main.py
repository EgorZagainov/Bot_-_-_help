import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import TOKEN
from handlear import start, add_notes_bot, all_note_inline


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router_start,
        add_notes_bot.router_add_note,
        all_note_inline.router_all_note


    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())