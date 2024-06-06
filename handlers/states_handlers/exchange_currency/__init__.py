__all__ = ('router', )

from aiogram import Router

from .another_first_cur import router as another_first_router
from .another_second_cur import router as another_second_router
from .second_cur import router as second_router
from .first_cur import router as first_router
from .count_money import router as count_router

router = Router(name=__name__)

router.include_router(another_first_router)
router.include_router(another_second_router)
router.include_router(second_router)
router.include_router(first_router)
router.include_router(count_router)
