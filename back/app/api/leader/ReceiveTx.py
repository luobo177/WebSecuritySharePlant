from fastapi import APIRouter,Request
from back.app.core.tool.verify_signature import verify_signature
from back.app.core.tx.BaseTx import BaseTx

router = APIRouter()

##receiveTx函数把接收到的tx（dict）转化成BaseTx，并放入pool中

@router.post('/tx')
def receiveTx(tx:dict,request:Request):
    try:
        tx = BaseTx.from_dict(tx)
    except Exception:
        return {"status": 400, "message": "bad format"}

    if not verify_signature(tx.sender, tx.tx_hash, tx.signature):
        return {"status": 400, "message": "invalid signature"}
    leader = request.app.state.leader
    leader.LeaderService.pool.add(tx)
    return {
    "status": "ok",
    "tx_hash": tx.tx_hash
    }