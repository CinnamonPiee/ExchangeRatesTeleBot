from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from utils.get_flag import get_flag


def back_button_reply_kb() -> ReplyKeyboardMarkup:
	builder = ReplyKeyboardBuilder()
	builder.button(text='Back')
	
	builder.adjust(1)

	return builder.as_markup(resize_keyboard=True)