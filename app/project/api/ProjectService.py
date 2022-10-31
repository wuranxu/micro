import base64

from klose.config import Config
from klose.excpetions.AuthException import AuthException
from klose.excpetions.RpcError import RpcError
from klose.model import async_session
from klose.request.fatcory import PityResponse
from klose.third_party.oss import OssClient
from klose.utils.client import RpcClient
from klose.utils.context import Interceptor, Context

from curd.ProjectDao import ProjectDao
from curd.ProjectRoleDao import ProjectRoleDao
from dto.project import ListProjectDto, ProjectForm, CustomDto, ProjectAvatarDto, ProjectRoleForm, ProjectRoleEditForm, \
    PermissionDto
from model.project_role import ProjectRole
from proto.project_pb2 import ListProjectResponseDto, ListProjectResponseData, ProjectModel, Response, \
    QueryProjectResponseDto, QueryProjectData, ProjectDto, ProjectRoleDto, ProjectAvatarResponseDto, \
    PermissionResponseDto
from proto.project_pb2_grpc import projectServicer


class ProjectServiceApi(projectServicer):

    @Interceptor(ListProjectDto, ListProjectResponseDto)
    async def list(self, request, context):
        """
        获取项目列表
        """
        user = Context.get_user(context)
        result, total = await ProjectDao.list_project(user.id, user.role, request.page, request.size, request.name)
        data = PityResponse.from_orm_list(result, ProjectModel)
        return ListProjectResponseData(data=data, total=total)

    @Interceptor(ProjectForm, Response, role=Config.MANAGER)
    async def insert(self, request, context):
        user = Context.get_user(context)
        await ProjectDao.add_project(user_id=user.id, **request.dict())

    @Interceptor(ProjectForm, Response)
    async def update(self, request, context):
        user = Context.get_user(context)
        await ProjectDao.update_project(user_id=user.id, role=user.role, **request.dict())

    @Interceptor(CustomDto, QueryProjectResponseDto)
    async def query(self, request, context):
        user = Context.get_user(context)
        data, roles = await ProjectDao.query_project(request.id)
        await ProjectRoleDao.access(user.id, user.role, roles, data)
        return QueryProjectData(project=PityResponse.from_orm(data, ProjectDto()),
                                roles=PityResponse.from_orm_list(roles, ProjectRoleDto))

    @Interceptor(ProjectAvatarDto, ProjectAvatarResponseDto)
    async def updateAvatar(self, request, context):
        """
        更新项目头像
        """
        content = base64.b64decode(request.content.split("base64,")[-1])
        suffix = request.filename.split(".")[-1]
        user = Context.get_user(context)
        filepath = f"project_{request.project_id}.{suffix}"
        system_service = await RpcClient.get_instance("system")
        resp = await system_service.getSystemConfig({}, metadata=context.invocation_metadata())
        if resp.get("code", 0) != 0:
            raise RpcError(f"获取系统配置失败: {resp.get('msg')}")
        client = OssClient.get_oss_client(resp.get("data").get("oss"))
        file_url, _ = await client.create_file(filepath, content, base_path="avatar")
        await ProjectDao.update_avatar(request.project_id, user.id, user.role, file_url)
        return file_url

    @Interceptor(CustomDto, Response)
    async def delete(self, request, context):
        user = Context.get_user(context)
        async with async_session() as session:
            async with session.begin():
                # 事务开始
                owner = await ProjectDao.is_project_admin(session, request.id, user.id)
                if not owner and user.role != Config.ADMIN:
                    raise PermissionError
                await ProjectDao.delete_record_by_id(session, user.id, request.id, session_begin=True)
                # 有可能项目没有测试计划 2022-03-14 fixed bug
                # TODO 待测试计划服务编写完成
                # await PityTestPlanDao.delete_record_by_id(session, user_info['id'], projectId, key="project_id",
                #                                           exists=False, session_begin=True)

    @Interceptor(ProjectRoleForm, Response)
    async def insertRole(self, request, context):
        user = Context.get_user(context)
        query = await ProjectRoleDao.query_record(user_id=request.user_id, project_id=request.project_id,
                                                  deleted_at=0)
        if query is not None:
            raise Exception("该用户已存在")
        await ProjectRoleDao.has_permission(request.project_id, request.project_role, user.id, user.role)
        model = ProjectRole(**request.dict(), create_user=user.id)
        await ProjectRoleDao.insert(model=model, log=True)

    @Interceptor(ProjectRoleEditForm, Response)
    async def updateRole(self, request, context):
        user = Context.get_user(context)
        await ProjectRoleDao.update_project_role(request, user.id, user.role)

    @Interceptor(CustomDto, Response)
    async def deleteRole(self, request, context):
        user = Context.get_user(context)
        await ProjectRoleDao.delete_project_role(request.id, user.id, user.role)

    @Interceptor(PermissionDto, PermissionResponseDto)
    async def checkPermission(self, request, context):
        try:
            await ProjectRoleDao.read_permission(**request.dict())
            return True
        except AuthException:
            return False
