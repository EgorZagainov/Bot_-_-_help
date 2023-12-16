from aiogram import Router, types, F, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import bot

router_admin = Router()


@router_admin.message(Command("admin"))
async def cmd_inline_url(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Bot is stopping", callback_data='stop')
        )
    builder.row(types.InlineKeyboardButton(
        text="Contacts",callback_data='contact')
        )
    builder.row(types.InlineKeyboardButton(
        text="sqlite3", url='tg://resolve?domain=telegram')
    )
    await message.answer(
        'Admin panel', reply_markup=builder.as_markup(),
    )



@router_admin.callback_query (F.data == 'contact')
async def cmd_contact(callback: types.CallbackQuery, bot: Bot):
    builder_admin = InlineKeyboardBuilder()
    builder_admin.row(types.InlineKeyboardButton(
        text="YouTube", url='https://www.youtube.com/')
        )
    builder_admin.row(types.InlineKeyboardButton(
        text="Контакты, Админа",callback_data='Number')
        )
    builder_admin.row(types.InlineKeyboardButton(
        text="Telegram", url='tg://resolve?domain=telegram')
    )
    await callback.message.answer(
        'Admin contacts', reply_markup=builder_admin.as_markup(),
    )
    await callback.answer()


@router_admin.callback_query(F.data == 'Number')
async def cmd_inline_admin(callback: types.CallbackQuery):
    await callback.message.answer("+7 987-727-57-33")
    await callback.answer()


