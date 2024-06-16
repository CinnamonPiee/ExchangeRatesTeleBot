from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils import markdown


router = Router(name=__name__)


@router.message(F.text == 'Help ❓')
@router.message(Command('help'))
async def help_handler(message: Message):
	await message.answer(
		text=f"{markdown.hbold("I'm a currency exchange bot.\n")}" \
			 "You can send the /help\n"\
			 "command at any time and find\n"\
			 "out all the information about\n"\
			 "me. If you need to return to\n"\
			 "the main menu, issue the /start\n"\
			 "command. I have a built-in and\n"\
			 "standard command /user_info\n"\
			 "so that you can find out\n"\
			 "information about your account.\n"\
			 "I also have registration using\n"\
			 "the /registration command, but\n"\
			 "it is NOT REQUIRED!!!\n"\
			)