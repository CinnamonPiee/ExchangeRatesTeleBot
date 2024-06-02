from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router(name=__name__)


@router.message(Command('user_info'))
async def user_info_handler(message: Message):
	await message.answer(text=f'Hello, {message.from_user.first_name}!\n' \
					  'This is your info: \n' \
					  f'Your id: {message.from_user.id}\n' \
					  f'Is bot: {message.from_user.is_bot}\n' \
					  f'First name: {message.from_user.first_name}\n' \
					  f'Last name: {message.from_user.last_name}\n' \
					  f'Username: {message.from_user.username}\n' \
					  f'Language code: {message.from_user.language_code}\n' \
					  f'Is premium: {message.from_user.is_premium}')
