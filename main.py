import asyncio
import logging
import sys


from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode


from config import TOKEN
from handlers import start, add_notes_bot, all_note_inline, del_note_bot, admin, inline


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        start.router_start,
        add_notes_bot.router_add_note,
        all_note_inline.router_all_note,
        del_note_bot.router_delete_note,
        admin.router_admin,
        inline.router_inline,
    )

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())