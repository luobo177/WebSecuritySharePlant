import time
import hashlib

class BaseChain:
    def __init__(self):
        self.chain = []


class BaseBlock:
    def __init__(self,tx:list,submitter:str):
        self.tx = tx
        self.submitter = submitter
        self.timestamp = int(time.time())
        self.block_hash = hashlib.sha256()
