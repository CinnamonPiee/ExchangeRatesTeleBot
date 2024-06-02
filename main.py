import logging
import asyncio

from config_data.config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram import Router
from handlers.default_handlers import echo, help, start, media_handlers
from handlers import router as main_router


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

router = Router()


async def main():
	logging.basicConfig(level=logging.INFO)
	dp.include_routers(main_router)
	await dp.start_polling(bot)


if __name__ == '__main__':
	asyncio.run(main())