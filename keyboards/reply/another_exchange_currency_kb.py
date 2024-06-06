from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from utils.get_flag import get_flag


def another_exchange_rates_reply_kb() -> ReplyKeyboardMarkup:
	builder = ReplyKeyboardBuilder()
	builder.button(text=f'KAZ {get_flag('KZ')}')
	builder.button(text=f'UKR {get_flag('UA')}')
	builder.button(text='Back')
	
	builder.adjust(2, 1)

	return builder.as_markup(resize_keyboard=True)