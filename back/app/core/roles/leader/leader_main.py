from time import sleep

from fastapi import FastAPI, APIRouter
import uvicorn
from back.app.core.tx.TxPool import TxPool
from back.app.servece.leader_serverce import LeaderService
from back.app.api.leader.router import router as leaderrouter
from back.app.core.roles.leader.Leader import Leader
def leader_main():
    app = FastAPI()
    leader = Leader()

    app.state.leader = leader

    ##注册路由
    app.include_router(leaderrouter)

    ##启动http服务
    uvicorn.run(app, host="0.0.0.0", port=9000)
    while True:
        leader.LeaderService.try_make_block()
        sleep(0.5)
if __name__ == '__main__':
    leader_main()