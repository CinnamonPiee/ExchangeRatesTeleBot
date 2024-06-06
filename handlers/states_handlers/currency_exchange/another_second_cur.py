from aiogram import Router, F

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.exchange_rates import ExchangeRates
from keyboards.reply.exchange_rates_reply_kb import exchange_rates_reply_keyboard
from keyboards.reply.another_exchange_rates_reply_kb import another_exchange_rates_reply_kb
from keyboards.reply.back_button import back_button_reply_kb
from config_data.config import ANOTHER_CUR_DATA


router = Router(name=__name__)


@router.message(ExchangeRates.another_rate_second, F.text.in_(ANOTHER_CUR_DATA))
async def another_cur(message: Message, state: FSMContext):
	await state.update_data(second_rate=message.text)
	await state.set_state(ExchangeRates.count_money)
	await message.answer(
		text='Ok. Now write how much money you need to exchange.',
		reply_markup=back_button_reply_kb(),
		)


@router.message(ExchangeRates.another_rate_second, F.text == 'Back')
async def another_cur_back(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.second_rate)
	await message.answer(
		text='Ok. Now let`s choose second currency to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
		)
	

@router.message(ExchangeRates.another_rate_second)
async def another_cur_back_not(message: Message):
	await message.answer(
		text='Sorry, I didn`t understand you!',
		reply_markup=another_exchange_rates_reply_kb(),
	)