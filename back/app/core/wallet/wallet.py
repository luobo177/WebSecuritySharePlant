import json
from dataclasses import asdict

from ecdsa import SigningKey, SECP256k1

from back.app.core.tool.hash import hash_tx
from back.app.core.tool.signature import sign_attack_tx
from back.app.core.tool.verify_hash import verify_hash
from back.app.core.tx.Attack_tx import AttackTx
import time
import os

WALLET_PATH="./data/wallet.json"


def exists():
    return os.path.exists(WALLET_PATH)


class Wallet:
    def __init__(self):
        self.public_key = None
        self.private_key = None
        if exists():
            self.load()
        else:
            self.generate()
            self.save()
        self.nonce = 0

    def load(self):
        with open(WALLET_PATH,"r",encoding="utf-8") as f:
            data = json.load(f)
            self.private_key = data["private_key"]
            self.public_key = data["public_key"]
            
    def generate(self):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.verifying_key
        self.private_key = sk.to_string().hex()
        self.public_key = vk.to_string().hex()

    def save(self):
        os.makedirs(os.path.dirname(WALLET_PATH), exist_ok=True)
        with open(WALLET_PATH, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "private_key": self.private_key,
                    "public_key": self.public_key
                },
                f,
                indent=2
            )

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


