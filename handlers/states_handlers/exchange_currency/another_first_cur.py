from aiogram import Router, F

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.fsm.state import any_state

from states.exchange_currency import ExchangeRates
from keyboards.reply.exchange_currency_kb import exchange_rates_reply_keyboard
from keyboards.reply.another_exchange_currency_kb import another_exchange_rates_reply_kb
from config_data.config import ANOTHER_CUR_DATA, CURRENCY_DATA


router = Router(name=__name__)


@router.message(ExchangeRates.another_rate_first, F.text.in_(ANOTHER_CUR_DATA))
async def another_cur(message: Message, state: FSMContext):
	CURRENCY_DATA.append(message.text)
	await state.update_data(first_rate=message.text)
	await state.set_state(ExchangeRates.second_rate)
	await message.answer(
		text='\n'\
			f'\t{CURRENCY_DATA[0]} -->\t\n'\
			 '\n'
			 'Ok. Now let`s choose second currency to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
		)


@router.message(ExchangeRates.another_rate_first, F.text == 'Back')
async def another_cur_back(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.first_rate)
	await message.answer(
		text='Choose currency what you want to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
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
	

@router.message(ExchangeRates.another_rate_first)
async def another_cur_back_not(message: Message):
	await message.answer(
		text='Sorry, I didn`t understand you!',
		reply_markup=another_exchange_rates_reply_kb(),
	)