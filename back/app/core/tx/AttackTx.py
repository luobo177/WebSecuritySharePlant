from dataclasses import dataclass
from typing import Any

@dataclass
class AttackPayLoad:
    Attack_type: str
    Source: str
    Destination: str
    level: str
    Detail: dict[str, Any]

    def to_payload(self) -> dict:
        return {
            "attack_type": self.Attack_type.lower(),
            "source": self.Source,
            "destination": self.Destination,
            "level": self.level.lower(),
            "detail": self.Detail
        }

