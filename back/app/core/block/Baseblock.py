import time
import hashlib

from back.app.core.tool.hash import hash_
from back.app.core.tool.signature import sign_tx

GENESIS_HASH = "0" * 64

class BaseChain:
    def __init__(self):
        self.chain = []

    def get_last_block_hash(self):
        if not self.chain:
            return GENESIS_HASH
        return self.chain[-1].block_hash


class BaseBlock:
    def __init__(self,pre_hash,txs):
        self.prev = pre_hash
        self.tx_hash = hash_(txs)
        self.signature = None
        self.timestamp = int(time.time())
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        raw = f"{self.prev.hash}{self.tx_hash}{self.timestamp}"
        return hashlib.sha256(raw.encode()).hexdigest()
