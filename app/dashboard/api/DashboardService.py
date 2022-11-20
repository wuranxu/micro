from datetime import datetime, timedelta

from klose.utils.client import RpcClient
from klose.utils.context import Context, Interceptor

from curd.dashboard import DashboardDao
from proto.dashboard_pb2 import WorkspaceResponse, WorkSpaceData
from proto.dashboard_pb2_grpc import dashboardServicer


class DashboardServiceApi(dashboardServicer):

    @Interceptor(None, WorkspaceResponse)
    async def statistics(self, request, context):
        """
        查询统计首页信息
        :param request:
        :param context:
        :return:
        """
        end = datetime.today()
        start = datetime.today() - timedelta(days=6)
        rank = await DashboardDao.query_user_case_rank()
        count, data = await DashboardDao.get_statistics_data(start, end)
        report_data = await DashboardDao.get_report_statistics(start, end)
        # online = ws_manage.get_clients()
        # return Context.success_json(dict(count=count, data=data, rank=rank, report=report_data))

    @Interceptor(None, WorkspaceResponse)
    async def workspace(self, request, context):
        """
        获取用户工作台数据
        :param request:
        :param context:
        :return:
        """
        user = Context.get_user(context)
        project_client = await RpcClient.get_instance("project")
        resp = await project_client.queryUserProjectAmount({}, metadata=context.invocation_metadata())
        if resp.get("code", 0) != 0:
            raise Exception(f"查询用户项目数量失败, {resp.get('msg')}")
        count = resp.get("data")
        rank = await DashboardDao.query_user_case_list()
        now = datetime.now()
        weekly_case = await DashboardDao.query_weekly_user_case(user.id, (now - timedelta(days=7)), now)
        case_count, user_rank = rank.get(str(user.id), [0, 0])
        return WorkSpaceData(project_count=count, case_count=case_count,
                             weekly_case=weekly_case,
                             user_rank=user_rank, total_user=len(rank))
