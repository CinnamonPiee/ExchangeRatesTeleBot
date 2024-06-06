from aiogram import Router, F

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.fsm.state import any_state

from states.exchange_currency import ExchangeRates
from keyboards.reply.exchange_currency_kb import exchange_rates_reply_keyboard
from keyboards.reply.another_exchange_currency_kb import another_exchange_rates_reply_kb
from keyboards.reply.back_button_kb import back_button_reply_kb
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
	

@router.message(Command('cancel'), any_state)
@router.message(F.text == 'cancel', any_state)
async def cancel_handler(message: Message, state: FSMContext) -> None:
	current_state = await state.get_state()
	if current_state is None:
		await message.reply(
			text='OK, but nothing was going on.',
			reply_markup=ReplyKeyboardRemove())
		return
	
	await state.clear()
	await message.answer(
		text='Cancelled state.',
		reply_markup=ReplyKeyboardRemove(),
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