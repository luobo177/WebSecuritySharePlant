import hashlib
import json


def hash_(tx_dict:dict) -> str:
    canonical = json.dumps(tx_dict, sort_keys=True,separators=(",",":"))
    return hashlib.sha256(canonical.encode()).hexdigest()