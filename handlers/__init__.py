__all__ = ('router', )

from aiogram import Router

from .default_handlers import router as default_router

router = Router(name=__name__)

router.include_router(default_router)