from http.client import HTTPException
from fastapi import APIRouter, HTTPException

from back.app.core.model.user import RegisterRequest
from back.app.servece.Register import register_user

router = APIRouter(prefix='/api/user')

@router.post('/register')
def register_user_api(req: RegisterRequest):
    try:
        return register_user(req)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))