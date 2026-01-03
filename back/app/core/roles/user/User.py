from datetime import time

from back.app.core.tool.hash import hash_
from back.app.core.tx.AttackTx import AttackPayLoad
from back.app.core.wallet.wallet import Wallet
import requests
import time
from back.app.config import SERVER_ADDR
from back.app.servece.TxService import create_attack_tx
from back.app.servece.UserDB import create_attack_tx_to_DB, init_User


def get_leader_info():
    return {
        "addr": "http://127.0.0.1:9000",
        "pubkey": "leader_pubkey_mock"
    }
    ##resp = requests.get(f"{SERVER_ADDR}/leader_info")
    # return resp.json()

def send_tx(tx):   ##将消息发给leader，让其打包
    leader_info=get_leader_info()
    tx = tx.to_dict()
    try:
        resp = requests.post(f"{leader_info['addr']}/tx",json=tx,timeout=2)
        return resp.status_code
    except Exception as e:
        print("send failed",e)
        return None



def register_to_center(public_key,sign_func,invite_code):
    payload = {
        "public_key": public_key,
        "invite_code": invite_code,
        "timestamp": int(time.time()),
    }
    payload_hash = hash_(payload)
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
        ##向center请求自己的role和id，并提交自己的invite_code和public_key
        Id,role = register_to_center(self.wallet.public_key, self.wallet.sign, self.invite_code)
        self.userId = Id
        self.role = role
        init_User()
        ##开始创建tx，并直接提交给leader，串行
        while True:
            tx = create_attack_tx(self.wallet,AttackPayLoad)
            create_attack_tx_to_DB(tx)
            send_tx(tx)
            time.sleep(0.1)










