from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.document, ~F.caption)
async def document_handler(message: Message):
	caption = "I can`t read this doc. Could you describe it please?"
	await message.reply_document(
		document=message.document.file_id,
		caption=caption)
	

@router.message(F.document, F.caption)
async def document_handler_with_caption(message: Message):
	caption = f"Cool document, your text: {message.caption}"
	await message.reply(text=caption)