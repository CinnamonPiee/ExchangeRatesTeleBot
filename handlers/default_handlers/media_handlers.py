from aiogram import Router, F
from aiogram.types import Message


router = Router()


any_media_handler = F.photo | F.video | F.document | F.sticker | F.gif | F.survey | F.voice


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


@router.message(F.document, ~F.caption)
async def document_handler(message: Message):
	caption = 'I can`t read this doc. Could you describe it please?'
	await message.reply_document(
		document=message.document.file_id,
		caption=caption)
	

@router.message(F.document, F.caption)
async def document_handler_with_caption(message: Message):
	caption = f'Cool document, your text: {message.caption}'
	await message.reply(text=caption)


@router.message(F.animation, ~F.caption)
async def animation_handler(message: Message):
	caption = 'I can`t see this animation. Could you describe it please?'
	await message.reply_animation(
		animation=message.animation.file_id,
		caption=caption)
	

@router.message(F.animation, F.caption)
async def animation_handler_with_caption(message: Message):
	caption = f'Cool animation, your text: {message.caption}'
	await message.reply(text=caption)


@router.message(F.audio, ~F.caption)
async def audio_handler(message: Message):
	caption = 'I can`t hear this audio. Could you describe it please?'
	await message.reply_audio(
		audio=message.audio.file_id,
		caption=caption)


@router.message(F.audio, F.caption)
async def audion_handler_with_caption(message: Message):
	caption = f'Cool audio, your text: {message.caption}'
	await message.reply(text=caption)


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