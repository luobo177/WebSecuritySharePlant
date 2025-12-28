from back.app.core.tx.TxPool import TxPool
from back.app.servece.leader_serverce import LeaderService

##创建全局tx_pool,全局leader_service,所有操作均导入app的leader_service进行操作

tx_pool = TxPool()
leader_service = LeaderService(tx_pool)
