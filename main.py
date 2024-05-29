import logging
import asyncio
 
from config_data.config import BOT_TOKEN
from aiogram import Bot, Dispatcher


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
	logging.basicConfig(level=logging.INFO)
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())