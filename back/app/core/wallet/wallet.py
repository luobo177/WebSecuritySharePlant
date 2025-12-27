import json
from ecdsa import SigningKey, SECP256k1
from back.app.core.tool.signature import sign_tx
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

    def sign(self,tx_hash):
        return sign_tx(self.private_key, tx_hash)

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



