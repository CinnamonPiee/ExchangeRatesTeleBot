from aiogram.fsm.state import State, StatesGroup


class ExchangeRates(StatesGroup):
	first_rate = State()
	second_rate = State()
	another_rate_first = State()
	another_rate_second = State()
	count_money = State()