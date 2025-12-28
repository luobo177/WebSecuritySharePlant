from dataclasses import dataclass
from enum import Enum
from typing import Any


class TxType(str, Enum):
    ATTACK = "attack"

@dataclass
class BaseTx:
    sender: str
    tx_type: TxType
    payload:dict[str, Any]
    timestamp: int
    nonce: int
    signature: str=""
    tx_hash:str=""

    @classmethod
    def from_dict(cls, tx):
        return cls(
            sender=tx["sender"],
            tx_type=tx["tx_type"],
            payload=tx["payload"],
            signature=tx["signature"],
            tx_hash=tx["tx_hash"],
            timestamp=tx["timestamp"],
            nonce=tx["nonce"],
        )