from back.app.core.tool.hash import hash_
from back.app.core.tool.verify_signature import verify_signature
from back.app.core.wallet.wallet import Wallet
from back.app.core.tx.BaseTx import BaseTx, TxType
import time
from dataclasses import asdict


def create_attack_tx(wallet:Wallet,payload):
    tx = BaseTx(wallet.public_key,
                TxType.ATTACK,
                payload,
                int(time.time()),
                wallet.nonce)
    tx_hash = hash_(asdict(tx))
    tx.tx_hash = tx_hash
    signature = wallet.sign(tx_hash)
    tx.signature = signature
    if verify_signature(wallet.public_key, tx_hash, signature):
        tx.signature = signature
        print("验证tx_hash的签名结果正常")
        wallet.nonce += 1
        return tx
    else:
        print("对tx_hash的签名出错，用公钥无法验证")
        return None
