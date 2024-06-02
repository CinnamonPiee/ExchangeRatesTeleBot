from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.contact, ~F.caption)
async def contact_handler(message: Message):
	caption = 'I can`t see this contact. Could you describe it please?'
	await message.reply_contact(
		contact=message.contact.file_id,
		caption=caption)


@router.message(F.contact, F.caption)
async def contact_handler_with_caption(message: Message):
	caption = f'Cool contact, your text: {message.caption}'
	await message.reply(text=caption)