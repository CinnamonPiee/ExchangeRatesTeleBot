from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.get_flag import get_flag


def exchange_rates_inline_keyboard() -> InlineKeyboardMarkup:
	button1 = InlineKeyboardButton(text=f'RUB {get_flag('RU')}', callback_data='rub')
	button2 = InlineKeyboardButton(text=f'USD {get_flag('US')}', callback_data='usd')
	button3 = InlineKeyboardButton(text=f'EUR {get_flag('EU')}', callback_data='eur')
	button4 = InlineKeyboardButton(text=f'GBR {get_flag('GB')}', callback_data='gbr')
	button5 = InlineKeyboardButton(text=f'GEO {get_flag('GE')}', callback_data='geo')
	button6 = InlineKeyboardButton(text='Another rate...', callback_data='another')
	button7 = InlineKeyboardButton(text='Back', callback_data='back')

	rows = []
	
	rows.append([button1])
	rows.append([button2])
	rows.append([button3])
	rows.append([button4])
	rows.append([button5])
	rows.append([button6])
	rows.append([button7])

	keyboard = InlineKeyboardMarkup(inline_keyboard=rows)

	return keyboard