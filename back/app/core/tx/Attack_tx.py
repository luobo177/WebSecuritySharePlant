from dataclasses import dataclass
from typing import Any

@dataclass
class AttackTx:
    sender: str
    payload:dict
    timestamp: int
    nonce: int
    signature: str = ""

@dataclass
class AttackPayLoad:
    Attack_type: str
    Source: str
    Destination: str
    level: str
    Detail: dict[str, Any]


