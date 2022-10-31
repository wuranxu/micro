import asyncio
import atexit

from klose.utils.serve import RpcService

from api.UserService import UserServiceApi
from proto import user_pb2_grpc, user_pb2


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


async def main():
    await RpcService.start("./service.yml", user_pb2_grpc.add_userServicer_to_server, UserServiceApi(), user_pb2)


if __name__ == "__main__":
    asyncio.run(main())
