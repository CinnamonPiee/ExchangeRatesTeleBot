__all__ = ('router', )

from aiogram import Router

from .start import router as start_router
from .help import router as help_router
from .media_handlers import router as media_router
from .echo import router as echo_router

router = Router(name=__name__)

router.include_router(start_router)
router.include_router(help_router)
router.include_router(media_router)
router.include_router(echo_router)