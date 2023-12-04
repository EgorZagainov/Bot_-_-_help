from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.markdown import hbold



router_add_note = Router()


ADD_NOTE = []
TIME_NOTE = []



class Note(StatesGroup):
    add_note = State()
    time_note = State()




@router_add_note.message(Command("add_note"))
async def cmd_robot(message: Message, state: FSMContext):
    await message.answer(
        text="какую задачу вы хотите создать:",
    )
    await state.set_state(Note.add_note)



@router_add_note.message(Note.add_note)
async def color_chosen(message: Message, state: FSMContext):
    await state.update_data(ADD_NOTE.append(message.text.lower()))
    await message.answer(
        text="Через сколько наоменить о задаче:",
    )
    await state.set_state(Note.time_note)




@router_add_note.message(Note.time_note)
async def function_chosen(message: Message, state: FSMContext):
    await state.update_data(TIME_NOTE.append((message.text.lower())))
    await message.answer(
        f"Хорошо вы  создали задачу для {*ADD_NOTE,}\n"
        f"Напоменание сработает через {*TIME_NOTE,} секунд"

    )


    await state.clear()