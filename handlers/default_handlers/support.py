from aiogram import Router, F
from aiogram.types import Message
from aiogram.utils import markdown
from keyboards.reply.start_kb import start_keyboard


router = Router(name=__name__)


@router.message(F.text == 'Support ⚙️')
async def support_handler(message: Message):
	await message.answer(
		text='You can write to the\n'
			 'developer about the problem\n'
			 'with the bot using this\n'
			 f'{markdown.hlink('link', 'https://t.me/Simon_Sh1')}.',
			 reply_markup=start_keyboard())
		
