from aiogram import Router, F
from aiogram.types import Message


router = Router(name=__name__)


@router.message(F.video, ~F.caption)
async def video_handler(message: Message):
	caption = 'I can`t see, sorry. Could you describe it please?'
	await message.reply_video(
		video=message.video.file_id, 
		caption=caption)


@router.message(F.video, F.caption)
async def video_handler_with_caption(message: Message):
	caption = f'Cool video, your text: {message.caption}'
	await message.reply(text=caption)