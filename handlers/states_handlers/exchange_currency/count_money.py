from aiogram import Router, F
from aiogram import types

from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.filters.command import Command

from states.exchange_currency import ExchangeRates
from keyboards.reply.exchange_currency_kb import exchange_rates_reply_keyboard
from keyboards.reply.back_button_kb import back_button_reply_kb


router = Router(name=__name__)


async def send_exchange_info(message: Message, data: dict) -> None:
	text = 'Your exchange results: \n' \
			f'First currency: {data['first_rate']}\n' \
			f'Second currency: {data['second_rate']}\n' \
			f'Count money: {data['count_money']}\n' \

	await message.answer(
		text=text,
		reply_markup=types.ReplyKeyboardRemove(),)


@router.message(ExchangeRates.count_money, F.text == 'Back')
async def count_money_back(message: Message, state: FSMContext):
	await state.set_state(ExchangeRates.second_rate)
	await message.answer(
		text='Ok. Now let`s choose second currency to exchange.',
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


@router.message(ExchangeRates.count_money, F.text)
async def count_money(message: Message, state: FSMContext):
	data = await state.update_data(count_money=message.text)
	await send_exchange_info(message, data)
	await state.clear()


@router.message(ExchangeRates.count_money)
async def count_money_not_understand(message: Message): 
	await message.answer(
		text='Sorry, I didn`t understand, please write how much money you need to exchange!',
		reply_markup=back_button_reply_kb())





