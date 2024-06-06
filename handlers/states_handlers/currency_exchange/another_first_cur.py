from aiogram import Router, F

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.exchange_rates import ExchangeRates
from keyboards.reply.exchange_rates_reply_kb import exchange_rates_reply_keyboard
from keyboards.reply.another_exchange_rates_reply_kb import another_exchange_rates_reply_kb
from config_data.config import ANOTHER_CUR_DATA


router = Router(name=__name__)


@router.message(ExchangeRates.another_rate_first, F.text.in_(ANOTHER_CUR_DATA))
async def another_cur(message: Message, state: FSMContext):
	await state.update_data(first_rate=message.text)
	await state.set_state(ExchangeRates.second_rate)
	await message.answer(
		text='Ok. Now let`s choose second currency to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
		)


@router.message(ExchangeRates.another_rate_first, F.text == 'Back')
async def another_cur_back(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.first_rate)
	await message.answer(
		text='Choose currency what you want to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
		)
	

@router.message(ExchangeRates.another_rate_first)
async def another_cur_back_not(message: Message):
	await message.answer(
		text='Sorry, I didn`t understand you!',
		reply_markup=another_exchange_rates_reply_kb(),
	)