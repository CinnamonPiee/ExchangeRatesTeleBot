from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def yes_or_no_keyboard() -> ReplyKeyboardMarkup:
	builder = ReplyKeyboardBuilder()
	builder.button(text="Yes")
	builder.button(text="No")
	return builder.as_markup(resize_keyboard=True)