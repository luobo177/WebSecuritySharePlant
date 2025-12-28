from back.app.core.tx.AttackTx import AttackPayLoad
from back.app.core.wallet.wallet import Wallet
from back.app.servece.TxService import create_attack_tx
from back.app.servece.UserDB import create_attack_tx_to_DB, init_User

wallet = Wallet()
raw = AttackPayLoad(
    Attack_type="SQL_INJECTION",
    Source="192.168.1.23",
    Destination="10.0.0.5:3306",
    level="HIGH",
    Detail={
        "parameter": "id",
        "payload": "' OR 1=1 --",
        "method": "GET",
        "url": "/login",
        "user_agent": "sqlmap/1.7.9"
    }
)

init_User()
payload=raw.to_payload()
tx = create_attack_tx(wallet,payload)
create_attack_tx_to_DB(tx)

