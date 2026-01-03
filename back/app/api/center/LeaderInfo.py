
from fastapi import APIRouter

router = APIRouter()
@router.get("/leader_info")
def leader_info():
    return {
        "leader_id": "...",
        "addr": "..."
    }
