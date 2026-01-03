from back.app.core.tx.TxPool import TxPool
from back.app.core.wallet import wallet
from back.app.servece.leader_serverce import LeaderService


class Leader:
    def __init__(self):
        self.wallet = wallet.Wallet()
        pool = TxPool()
        self.LeaderService = LeaderService(pool,wallet.sign_tx)



