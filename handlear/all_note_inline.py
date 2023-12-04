from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder


from add_notes_bot import ADD_NOTE



router_all_note = Router()




@router_all_note.message(Command("all_note"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    for i in range(len(ADD_NOTE)):
        b = str(i)
        builder.row(types.InlineKeyboardButton(
              text=ADD_NOTE[i], callback_data=b)
        )

    await message.answer(
        'Выберите ссылку', reply_markup=builder.as_markup(),
    )

