from back.app.core.tx.TxPool import TxPool


class LeaderService:
    def __init__(self,pool: TxPool):
        self.pool = pool
