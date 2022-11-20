import asyncio
import atexit

from klose.utils.serve import RpcService

from api.DashboardService import DashboardServiceApi
from proto import dashboard_pb2, dashboard_pb2_grpc


@atexit.register
def unregister():
    asyncio.run(RpcService.shutdown())


async def main():
    await RpcService.start("./service.yml", dashboard_pb2_grpc.add_dashboardServicer_to_server,
                           DashboardServiceApi(), dashboard_pb2)


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
