from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard():
	button1 = KeyboardButton(text="Exchange rates 💵")
	button2 = KeyboardButton(text="Support ⚙️")
	button3 = KeyboardButton(text="Help ❓")
	button4 = KeyboardButton(text="About Bot ❗️")
	button5 = KeyboardButton(text="Feedback 📧")

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1],
				[button2, button3],
				[button4, button5]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard