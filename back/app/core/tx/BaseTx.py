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