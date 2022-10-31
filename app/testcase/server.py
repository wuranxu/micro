import asyncio
import atexit

from klose.utils.serve import RpcService

from api.TestCaseService import TestCaseServiceApi
from proto import testcase_pb2, testcase_pb2_grpc


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


async def main():
    await RpcService.start("./service.yml", testcase_pb2_grpc.add_testcaseServicer_to_server, TestCaseServiceApi(),
                           testcase_pb2)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
