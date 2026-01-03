from back.app.api.leader.ReceiveTx import receiveTx
from back.app.core.roles.leader.leader_app import leader_service

tx_dict = {
    "sender": "8ea3aa6d82b7d7646234abd4bc85c077dd1d1d5f3b94b5e4499abf348980d33737025464abd116f71cdee119940e6eb6ebb156e96e5209aa2827a5bc82135330",
    "tx_type": "attack",
    "payload": {
        "attack_type": "sql_injection",
        "source": "192.168.1.23",
        "destination": "10.0.0.5:3306",
        "level": "high",
        "detail": {
            "parameter": "id",
            "payload": "' OR 1=1 --",
            "method": "GET",
            "url": "/login",
            "user_agent": "sqlmap/1.7.9"
        }
    },
    "timestamp": 1766938912,
    "nonce": 0,
    "signature": "fafdc7bf917576a84896b5551bfd3ca2d3aec65e1cd6fe63fc2e800d5c497c1eaafe3e8c1b0070a78be2d0a928a34fa507a2781b5fb32e230f76cdfebf7b0cb9",
    "tx_hash": "ba254db89cfbd43b49d0fc9ab2042027ed24db09130c4ea38bafcdcd817d20b7"
}


res = receiveTx(tx_dict)
print(leader_service.pool.all())

