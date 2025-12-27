from datetime import time
from back.app.core.test import payload
from back.app.core.tool.hash import hash_tx
from back.app.core.tx.BaseTx import BaseTx, TxType
from back.app.core.wallet.wallet import Wallet
import requests
import time
from back.app.config import SERVER_ADDR

def get_leader_info():
    resp = requests.get(f"{SERVER_ADDR}/leader_info")
    return resp.json()

def send_attack_tx(tx: BaseTx):   ##将消息发给leader，让其打包
    if tx.tx_type != TxType.ATTACK:
        raise ValueError('Invalid tx type')
    leader_info=get_leader_info()
    requests.post(f"{leader_info['addr']}/tx",json=tx)

def register_to_center(public_key,sign_func,invite_code):
    payload = {
        "public_key": public_key,
        "invite_code": invite_code,
        "timestamp": int(time.time()),
    }
    payload_hash = hash_tx(payload)
    signature = sign_func(payload_hash)
    payload["signature"] = signature

    resp = requests.post(f"{SERVER_ADDR}/api/user/register",json=payload,timeout=5)
    resp.raise_for_status()
    data=resp.json()
    user_id=data['user_id']
    role=data['role']
    return user_id,role


class User:
    def __init__(self):
        self.userId = None
        self.role = None
        self.wallet = Wallet()
        self.invite_code = None
        Id,role = register_to_center(self.wallet.public_key, self.wallet.sign, self.invite_code)










