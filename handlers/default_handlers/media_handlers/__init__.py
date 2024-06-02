__all__ = ('router', )

from aiogram import Router

from .animation_handler import router as animation_router
from .audio_handler import router as audio_router
from .contact_handler import router as contact_router
from .dice_handler import router as dice_router
from .document_handler import router as document_router
from .photo_handler import router as photo_router
from .video_handler import router as video_router

router = Router(name=__name__)

router.include_router(animation_router)
router.include_router(audio_router)
router.include_router(contact_router)
router.include_router(dice_router)
router.include_router(document_router)
router.include_router(photo_router)
router.include_router(video_router)