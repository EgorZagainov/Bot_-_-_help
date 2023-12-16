from aiogram import Router, types
from aiogram.filters import Command

router_my_id = Router()

@router_my_id.message(Command('get_my_id'))
async def get_my_id(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"Ваш user_id: {user_id}")