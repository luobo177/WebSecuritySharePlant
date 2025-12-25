from ecdsa import SigningKey, SECP256k1
from back.app.core.tx.Attack_tx import AttackTx
from back.app.core.wallet.wallet import Wallet
import requests

def get_leader_info():
    pass

def send_attack_tx(tx: AttackTx):
    leader_info=get_leader_info()
    leader_url = f"https://{leader_info['ip']}:{leader_info['port']}"
    requests.post(f"{leader_url}/submit_attack_tx",json=tx)

class User:
    def __init__(self):
        self.wallet = Wallet()





