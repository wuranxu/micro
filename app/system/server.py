import asyncio
import atexit

from klose.utils.serve import RpcService

from api.SystemService import SystemServiceApi
from proto import system_pb2_grpc, system_pb2


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


async def main():
    await RpcService.start("./service.yml", system_pb2_grpc.add_systemServicer_to_server, SystemServiceApi(),
                           system_pb2)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
