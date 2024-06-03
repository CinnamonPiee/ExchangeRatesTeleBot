__all__ = ('router', )

from aiogram import Router

from .exchange_rates_keyboard import router as exchange_rates_router

router = Router(name=__name__)

router.include_router(exchange_rates_router)