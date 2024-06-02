from aiogram.types import Message
from aiogram import Router, F
from keyboards.inline.exchange_rates_inline_keyboard import exchange_rates_inline_keyboard


router = Router(name=__name__)


@router.message(F.text == 'Exchange rates 💵')
async def exchange_rates_buttons(message: Message):
	await message.answer(
		text='Choose rate what you need change: ',
		reply_markup=exchange_rates_inline_keyboard())