from back.app.core.block.Baseblock import BaseBlock, BaseChain
from back.app.core.tx.TxPool import TxPool



class LeaderService:
    def __init__(self,pool: TxPool,sign_func):
        self.pool = pool
        self.sign = sign_func
        self.blockchain = BaseChain()

    def try_make_block(self):
        txs = self.pool.package()
        pre_hash = self.blockchain.get_last_block_hash()
        block = BaseBlock(pre_hash,txs)
        block.signature = self.sign(block.block_hash.encode())
        print(block)
        return block