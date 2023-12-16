from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types, Bot, F



router_inline = Router()
@router_inline.message(Command("contacts"))
async def cmd_inline_url(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="YouTube", url='https://www.youtube.com/')
        )
    builder.row(types.InlineKeyboardButton(
        text="Контакты, Админа",callback_data='Number')
        )
    builder.row(types.InlineKeyboardButton(
        text="Telegram", url='tg://resolve?domain=telegram')
    )
    await message.answer(
        'Admin contacts', reply_markup=builder.as_markup(),
    )


@router_inline.callback_query(F.data == 'Number')
async def cmd_inline_admin(callback: types.CallbackQuery):
    await callback.message.answer("+7 987-727-57-33")
    await callback.answer()