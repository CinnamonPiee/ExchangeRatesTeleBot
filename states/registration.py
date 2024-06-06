from aiogram.fsm.state import State, StatesGroup


class Survey(StatesGroup):
	name = State()
	age = State()
	city = State()
	email = State()
	email_newsletter = State()
	number = State()