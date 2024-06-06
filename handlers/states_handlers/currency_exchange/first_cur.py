from aiogram import Router, F

from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.exchange_rates import ExchangeRates
from keyboards.reply.start_keyboard import start_keyboard
from keyboards.reply.exchange_rates_reply_kb import exchange_rates_reply_keyboard
from keyboards.reply.another_exchange_rates_reply_kb import another_exchange_rates_reply_kb
from config_data.config import DEFAULT_CUR_DATA


router = Router(name=__name__)


@router.message(F.text == 'Exchange rates 💵')
async def exchange_rates_start(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.first_rate)
	await message.answer(
		text='Choose currency what you want to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
		)
	

@router.message(ExchangeRates.first_rate, F.text.in_(DEFAULT_CUR_DATA))
async def first_rate(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.second_rate)
	await state.update_data(first_rate=message.text)
	await message.answer(
		text='Ok. Now let`s choose second currency to exchange.',
		reply_markup=exchange_rates_reply_keyboard(),
		)
	

@router.message(ExchangeRates.first_rate, F.text == 'Another rate...')
async def first_rate(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.another_rate_first)
	await message.answer(
		text='Another currency.',
		reply_markup=another_exchange_rates_reply_kb(),
		)
	

@router.message(ExchangeRates.first_rate, F.text == 'Back')
async def first_rate(message: Message, state: FSMContext):
	await message.answer(
		text='Maybe in next time...',
		reply_markup=start_keyboard())
	await state.clear()
	

@router.message(ExchangeRates.first_rate)
async def first_rate(message: Message): 
	await message.answer(
		text='Sorry, I didn`t understand, please choose currency!',
		reply_markup=exchange_rates_reply_keyboard(),
		)