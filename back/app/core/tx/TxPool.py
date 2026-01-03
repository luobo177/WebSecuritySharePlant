from collections import deque
from typing import List,Iterable, Optional

from back.app.core.tx.BaseTx import BaseTx
from back.app.core.tx.BaseTx import TxType


class TxPool:
    def __init__(self):
        self.pool = deque()

    def add(self, tx:BaseTx) -> None:
        self.pool.append(tx)

    def remove(self, tx):
        self.pool.remove(tx)

    def all(self) -> List[BaseTx]:
        return list(self.pool)

    def by_type(self,tx_type:TxType)->List[BaseTx]:
        return [tx for tx in self.pool if tx_type == tx_type]

    def package(self)->list[BaseTx]:
        n = 10
        txs = []
        for _ in range(min(n, len(self.pool))):
            tx = self.pool.popleft()
            txs.append(tx)
        return txs


