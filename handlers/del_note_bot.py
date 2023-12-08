from aiogram import Router, F, types, Bot
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.add_notes_bot import ADD_NOTE,TIME_NOTE,Note


router_delete_note = Router()



@router_delete_note.message(Command("del_note"))
async def cmd_inline(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
              text='Удалить все задачи', callback_data = "full_delete")
        )

    await message.answer(
        f'Нажмите на ту которую хотите удалить ', reply_markup=builder.as_markup(),
    )



@router_delete_note.callback_query(F.data == 'full_delete')
async def cmd_del(callback: types.CallbackQuery):
    ADD_NOTE.clear()
    TIME_NOTE.clear()
    await callback.answer('Вы удалили все задачи')


