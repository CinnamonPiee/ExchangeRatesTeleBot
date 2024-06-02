from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_keyboard():
	button1 = KeyboardButton(text='Exchange rates 💵')
	button2 = KeyboardButton(text='Country banks 🏦')
	button3 = KeyboardButton(text='Support ⚙️')
	button4 = KeyboardButton(text='Help ❓')
	button5 = KeyboardButton(text='About Bot ❗️')
	button6 = KeyboardButton(text='Feedback 📧')

	keyboard = ReplyKeyboardMarkup(
		keyboard=[[button1, button2], 
				  [button3, button4],
				  [button5, button6]],
		resize_keyboard=True,
		one_time_keyboard=True,)
    
	return keyboard