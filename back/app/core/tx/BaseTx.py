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
            tx_type=TxType(tx["tx_type"]),  # 👈 反序列化 Enum
            payload=tx["payload"],
            timestamp=tx["timestamp"],
            nonce=tx["nonce"],
            signature=tx.get("signature", ""),
            tx_hash=tx.get("tx_hash", ""),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "sender": self.sender,
            "tx_type": self.tx_type.value,    # 👈 Enum → str
            "payload": self.payload,
            "timestamp": self.timestamp,
            "nonce": self.nonce,
            "signature": self.signature,
            "tx_hash": self.tx_hash,
        }