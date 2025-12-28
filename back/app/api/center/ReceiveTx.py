from fastapi import APIRouter

router = APIRouter(prefix='/api/leader')
@router.post('/tx')
def receiveTx(tx):

