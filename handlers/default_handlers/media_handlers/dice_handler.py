from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.dice, ~F.caption)
async def dice_handler(message: Message):
	caption = 'I can`t hear this dice. Could you describe it please?'
	await message.reply_dice(
		dice=message.dice.file_id,
		caption=caption)


@router.message(F.dice, F.caption)
async def dice_handler_with_caption(message: Message):
	caption = f'Cool dice, your text: {message.caption}'
	await message.reply(text=caption)