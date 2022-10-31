import asyncio
import atexit

from klose.utils.serve import RpcService

from api.ProjectService import ProjectServiceApi
from proto import project_pb2, project_pb2_grpc


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


async def main():
    await RpcService.start("./service.yml", project_pb2_grpc.add_projectServicer_to_server, ProjectServiceApi(),
                           project_pb2)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
