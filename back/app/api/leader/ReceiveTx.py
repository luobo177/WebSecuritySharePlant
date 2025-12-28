from fastapi import APIRouter

from back.app.core.tool.verify_signature import verify_signature
from back.app.core.tx.BaseTx import BaseTx
from back.leader_app import leader_service

router = APIRouter(prefix='/api/leader')

##receiveTx函数把接收到的tx（dict）转化成BaseTx，并放入pool中

@router.post('/tx')
def receiveTx(tx:dict):
    try:
        tx = BaseTx.from_dict(tx)
    except Exception:
        return {"status": 400, "message": "bad format"}

    if not verify_signature(tx.sender, tx.tx_hash, tx.signature):
        return {"status": 400, "message": "invalid signature"}
    leader_service.pool.add(tx)
    return {
    "status": "ok",
    "tx_hash": tx.tx_hash
    }