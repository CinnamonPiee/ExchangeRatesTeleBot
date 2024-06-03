from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data == 'rub')
async def rub_callback(callback_query: CallbackQuery):
	await callback_query.answer(text='This is russian rate!')


@router.callback_query(F.data == 'usd')
async def usd_callback(callback_query: CallbackQuery):
	await callback_query.answer(text='This is American rate!')