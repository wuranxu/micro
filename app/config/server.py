import asyncio
import atexit

from klose.utils.serve import RpcService

from api.ConfigService import ConfigServiceApi
from proto import config_pb2_grpc, config_pb2


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


async def main():
    await RpcService.start("./service.yml", config_pb2_grpc.add_configServicer_to_server, ConfigServiceApi(), config_pb2)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
