__all__ = ('router', )

from aiogram import Router

from .survey import router as survey_router
from .exchange_currency import router as currency_router

router = Router(name=__name__)

router.include_router(survey_router)
router.include_router(currency_router)