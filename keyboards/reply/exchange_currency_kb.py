from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from utils.get_flag import get_flag


def exchange_rates_reply_keyboard() -> ReplyKeyboardMarkup:
	builder = ReplyKeyboardBuilder()
	builder.button(text=f"RUB {get_flag("RU")}")
	builder.button(text=f"USD {get_flag("US")}")
	builder.button(text=f"EUR {get_flag("EU")}")
	builder.button(text=f"GBP {get_flag("GB")}")
	builder.button(text=f"GEL {get_flag("GE")}")
	builder.button(text="Another rate...")
	builder.button(text="Back")
	
	builder.adjust(5, 2)

	return builder.as_markup(resize_keyboard=True)