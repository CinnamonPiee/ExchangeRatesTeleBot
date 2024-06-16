from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.animation, ~F.caption)
async def animation_handler(message: Message):
	caption = "I can`t see this animation. Could you describe it please?"
	await message.reply_animation(
		animation=message.animation.file_id,
		caption=caption)
	

@router.message(F.animation, F.caption)
async def animation_handler_with_caption(message: Message):
	caption = f"Cool animation, your text: {message.caption}"
	await message.reply(text=caption)