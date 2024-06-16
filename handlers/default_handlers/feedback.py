from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils import markdown
from keyboards.reply.start_kb import start_keyboard


router = Router(name=__name__)


@router.message(F.text == "Feedback 📧")
async def feedback_handler(message: Message):
	await message.answer(
		text="You can leave a comment on\n"
			 "this bot or express your deep\n"
			 "gratitude for the work of the\n"
			 f"developer using this {markdown.hlink("link", "https://t.me/Simon_Sh1")}.\n"
			 "You can also view the source\n"
			 f"code of this bot on {markdown.hlink("GitHub", "https://github.com/KellTuz/ExchangeRatesTeleBot")}.",
			 reply_markup=start_keyboard())