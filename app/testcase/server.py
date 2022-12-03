import asyncio
import atexit

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from klose.config import Config
from klose.utils.serve import RpcService

from api.TestCaseService import TestCaseServiceApi
from proto import testcase_pb2, testcase_pb2_grpc
from utils.scheduler import Scheduler


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


def init_scheduler():
    """
    初始化定时任务
    :return:
    """
    # SQLAlchemyJobStore指定存储链接
    job_store = {
        'default': SQLAlchemyJobStore(url=Config.SQLALCHEMY_DATABASE_URI, engine_options={"pool_recycle": 1500},
                                      pickle_protocol=3)
    }
    scheduler = AsyncIOScheduler()
    Scheduler.init(scheduler)
    Scheduler.configure(jobstores=job_store)
    Scheduler.start()


async def main():
    init_scheduler()
    await RpcService.start("./service.yml", testcase_pb2_grpc.add_testcaseServicer_to_server, TestCaseServiceApi(),
                           testcase_pb2)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
