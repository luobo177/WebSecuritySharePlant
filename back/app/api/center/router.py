from fastapi import APIRouter
from back.app.api.center.LeaderInfo import router as leader_info
from back.app.api.center.register import router as register_user_api

router = APIRouter(prefix = '/center')

router.include_router(leader_info)
router.include_router(register_user_api)