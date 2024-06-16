from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils import markdown
from keyboards.reply.start_kb import start_keyboard


router = Router(name=__name__)


@router.message(F.text == "About Bot ❗️")
async def about_handler(message: Message):
	await message.answer(
		text="The bot was created for\n"
			 "educational purposes by one\n"
			 "developer. The bot does not\n"
			 "carry out any commercial\n"
			 "activities. If you want to\n"
			 "help the developer, or you\n"
			 "find a problem with the bot,\n"
			 "you can contact it through the\n"
			 "'Support ⚙️'section.\n"
			 "Information on using the bot\n"
			 "can be found in the 'Help ❓'\n"
			 "section. Information about\n"
			 "currency exchange is taken\n"
			 f"from the website {markdown.hlink("TwelveData", "https://twelvedata.com/")}\n"
			 "Enjoy using it!",
			 reply_markup=start_keyboard()
			)
	