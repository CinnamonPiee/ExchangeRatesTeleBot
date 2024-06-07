from aiogram import Router, F

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.state import any_state

from states.exchange_currency import ExchangeRates
from keyboards.reply.back_button_kb import back_button_reply_kb
from keyboards.reply.exchange_currency_kb import exchange_rates_reply_keyboard
from keyboards.reply.another_exchange_currency_kb import another_exchange_rates_reply_kb
from config_data.config import DEFAULT_CUR_DATA, CURRENCY_DATA


router = Router(name=__name__)


@router.message(ExchangeRates.second_rate, F.text.in_(DEFAULT_CUR_DATA))
async def second_rate(message: Message, state: FSMContext):
	CURRENCY_DATA.append(message.text)
	await state.set_state(ExchangeRates.count_money)
	await state.update_data(second_rate=message.text)
	await message.answer(
		text='\n'\
			f'\t{CURRENCY_DATA[0]} --> {CURRENCY_DATA[1]}\t\n'\
			 '\n'
			 'Ok. Now write how much money you need to exchange.',
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


@router.message(ExchangeRates.second_rate, F.text == 'Another rate...')
async def second_rate(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.another_rate_second)
	await message.answer(
		text='Another currency.',
		reply_markup=another_exchange_rates_reply_kb(),
		)
	

@router.message(ExchangeRates.second_rate, F.text == 'Back')
async def second_rate(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.first_rate)
	await message.answer(
		text='Choose currency what you want to exchange.',
		reply_markup=exchange_rates_reply_keyboard()
		)
	

@router.message(ExchangeRates.second_rate)
async def second_rate(message: Message): 
	await message.answer(
		text='Sorry, I didn`t understand, please choose currency!',
		reply_markup=exchange_rates_reply_keyboard(),
		)