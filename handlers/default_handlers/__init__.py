__all__ = ('router', )

from aiogram import Router

from .start import router as start_router
from .help import router as help_router
from .about_bot import router as about_router
from .support import router as support_router
from .feedback import router as feedback_router
from .media_handlers import router as media_router
from .cancel import router as cancel_router
from .echo import router as echo_router

router = Router(name=__name__)

router.include_router(start_router)
router.include_router(help_router)
router.include_router(media_router)
router.include_router(cancel_router)
router.include_router(about_router)
router.include_router(support_router)
router.include_router(feedback_router)

# this router is last!
router.include_router(echo_router)