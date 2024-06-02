from aiogram import Router, F
from aiogram.types import Message
from config_data.config import ADMIN_ID


router = Router(name=__name__)


@router.message(F.from_user.id.in_({42, int(ADMIN_ID)}), F.text == 'statistic')
async def statistic_admin_message(message: Message):
	await message.answer(text='Hello, Admin!')