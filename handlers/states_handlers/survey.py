from aiogram import Router, F
from aiogram import types

from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from email_validator import validate_email
from states.survey import Survey
from keyboards.reply.yes_or_no_kb import yes_or_no_keyboard


router = Router(name=__name__)


@router.message(Command('survey'))
async def survey_start(message: Message, state: FSMContext):
	await state.set_state(Survey.name)
	await message.answer(
		text='Welcome to our weekly survey! What`s your name?',
		reply_markup=types.ReplyKeyboardRemove(),) 
	

@router.message(Survey.name, F.text)
async def survey_name(message: Message, state: FSMContext):
	await state.set_state(Survey.age)
	await state.update_data(name=message.text)
	await message.answer(
		text=f'Hello, {message.text}! Now write me please your age.',)
	

@router.message(Survey.name)
async def survey_name_invalid_content_type(message: Message):
	await message.answer(
		text='Sorry, I didn`t understand, send your full name as text.',)
	

@router.message(Survey.age)
async def survey_age(message: Message, state: FSMContext):
	await state.set_state(Survey.city)
	await state.update_data(age=message.text)
	await message.answer(
		text=f'You are so young in {message.text}. Now write me your city.',)
	

@router.message(Survey.city)
async def survey_city(message: Message, state: FSMContext):
	await state.set_state(Survey.email)
	await state.update_data(city=message.text)
	await message.answer(
		text=f'I never been in {message.text}. Now write me your email.',)
	

@router.message(Survey.email, F.text.cast(validate_email).normalized.as_("email"))
async def survey_email(
	message: Message, 
	state: FSMContext,
	email: str,):
	await state.update_data(email=email)
	await state.set_state(Survey.email_newsletter)
	await message.answer(
		text=f'Cool, your email is now {email}.'
			  'Would you like to be contacted in future?',
			  reply_markup=yes_or_no_keyboard(),)
	

@router.message(Survey.email)
async def survey_email_invalid_content_type(message: Message):
	await message.answer(
		text=f'Invalid email, please try again.',)
	

@router.message(Survey.email_newsletter, F.text.casefold() == 'yes')
async def survey_yes(message: Message, state: FSMContext):
	await state.set_state(Survey.number)
	await state.update_data(newsletter_ok=True)
	await message.answer(
		text='Cool.  Let`s write me your number.',)


@router.message(Survey.email_newsletter, F.text.casefold() == 'no')
async def survey_no(message: Message, state: FSMContext):
	await state.set_state(Survey.number)
	await state.update_data(newsletter_ok=False)
	await message.answer(
		text='Ok. Let`s write me your number.',)


@router.message(Survey.email_newsletter)
async def survey_not_understand(message: Message):
	await message.answer(
		text='Sorry, I didn`t understand, please send "yes" or "no".',
		reply_markup=yes_or_no_keyboard())
	

async def send_survey_results(message: Message, data: dict) -> None:
	text = 'Your survey results:\n\n' \
		   f'Name: {data['name']}\n' \
		   f'Age: {data['age']}\n' \
		   f'City: {data['city']}\n' \
		   f'Email: {data['email']}\n' \
		   f'Newsletter: {data['newsletter_ok']}\n' \
		   f'Phone number: {data['number']}\n'
	await message.answer(
		text=text,
		reply_markup=types.ReplyKeyboardRemove(),)
	

@router.message(Survey.number)
async def survey_number(message: Message, state: FSMContext):
	data = await state.update_data(number=message.text)
	await send_survey_results(message, data)
	await state.clear()
	
	

