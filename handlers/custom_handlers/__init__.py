__all__ = ('router', )

from aiogram import Router

from .admin_handlers import router as admin_router
from .user_info_handler import router as user_info_router

router = Router(name=__name__)

router.include_router(admin_router)
router.include_router(user_info_router)
