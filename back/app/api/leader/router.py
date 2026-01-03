from fastapi import APIRouter

from .ReceiveTx import router as receive

router = APIRouter()
router.include_router(receive)
