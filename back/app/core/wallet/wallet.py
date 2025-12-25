from dataclasses import asdict
from back.app.core.tool.hash import hash_tx
from back.app.core.tool.signature import sign_attack_tx
from back.app.core.tool.verify_hash import verify_hash
from back.app.core.tx.Attack_tx import AttackTx
import time




class Wallet:
    def __init__(self,private_key,public_key):
        self.private_key = private_key
        self.public_key = public_key
        self.nonce = 0

    def create_attack_tx(self,payload):
        tx = AttackTx(self.public_key,payload,int(time.time()),self.nonce)
        tx_hash = hash_tx(asdict(tx))
        signature = sign_attack_tx(self.private_key,tx_hash)
        if verify_hash(self.public_key,tx_hash,signature):
            tx.signature = signature
            print("验证tx_hash的签名结果正常")
            self.nonce += 1
            return tx
        else:
            print("对tx_hash的签名出错，用公钥无法验证")
            return None


