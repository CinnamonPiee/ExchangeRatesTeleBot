from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state


router = Router(name=__name__)


@router.message(Command("cancel"), any_state)
@router.message(F.text == "cancel", any_state)
async def cancel_handler(message: Message, state: FSMContext) -> None:
	current_state = await state.get_state()
	if current_state is None:
		await message.reply(
			text="OK, but nothing was going on.",
			reply_markup=ReplyKeyboardRemove())
		return
	
	await state.clear()
	await message.answer(
		text="Cancelled state.",
		reply_markup=ReplyKeyboardRemove(),
	)