from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command


router = Router(name=__name__)


@router.message(F.text == 'Help ❓')
@router.message(Command('help'))
async def help_handler(message: Message):
	await message.answer(text='I`am echo bot')