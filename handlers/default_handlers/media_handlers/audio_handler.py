from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.audio, ~F.caption)
async def audio_handler(message: Message):
	caption = "I can`t hear this audio. Could you describe it please?"
	await message.reply_audio(
		audio=message.audio.file_id,
		caption=caption)


@router.message(F.audio, F.caption)
async def audion_handler_with_caption(message: Message):
	caption = f"Cool audio, your text: {message.caption}"
	await message.reply(text=caption)