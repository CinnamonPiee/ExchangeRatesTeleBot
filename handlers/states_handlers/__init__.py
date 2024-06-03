from aiogram import Router

router = Router(name=__name__)

from .survey import router as survey_router

router.include_router(survey_router)