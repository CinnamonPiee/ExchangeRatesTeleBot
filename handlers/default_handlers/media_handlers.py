from aiogram import Router, F
from aiogram.types import Message


router = Router()


any_media_handler = F.photo | F.video | F.document | F.sticker | F.gif


@router.message(any_media_handler, ~F.caption)
async def media_handler(message: Message):
	await message.reply(text='I don`t understand you, sorry!. Could you describe it please?')


@router.message(any_media_handler, F.caption)
async def media_handler_with_caption(message: Message):
	await message.answer(text='Sorry, i don`t work with this!')