__all__ = ('router', )

from aiogram import Router

from .default_handlers import router as default_router
from .custom_handlers import router as custom_router

router = Router(name=__name__)

router.include_router(custom_router)
router.include_router(default_router)