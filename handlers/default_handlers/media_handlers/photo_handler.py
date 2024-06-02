from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.photo, ~F.caption)
async def photo_handler(message: Message):
	caption = 'I can`t see, sorry. Could you describe it please?'
	await message.reply_photo(
		photo=message.photo[-1].file_id, 
		caption=caption)
	

@router.message(F.photo, F.caption)
async def photo_handler_with_caption(message: Message):
	caption = f'Cool photo, your text: {message.caption}'
	await message.reply(text=caption)