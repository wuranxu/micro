import json

from klose.config import Config
from klose.model import async_session, db_helper, DatabaseHelper
from klose.request.fatcory import PityResponse
from klose.third_party.Redis import PityRedisManager
from klose.utils.context import Interceptor, Context

from curd.DbConfigDao import DbConfigDao, PitySQLHistoryDao
from curd.EnvironmentDao import EnvironmentDao
from curd.GConfigDao import GConfigDao
from curd.PityGatewayDao import PityGatewayDao
from curd.RedisConfigDao import PityRedisConfigDao
from dto.address import PityAddressForm, CustomDto, PityGatewayDto
from dto.database import QueryDatabaseDto, DatabaseDto, TestDatabaseDto, RunSQLCommandDto, QuerySQLHistoryDto
from dto.environment import EnvironmentDto, QueryEnvironmentDto
from dto.gconfig import QueryGConfigDto, GConfigDto
from dto.redis_config import QueryRedisDto, RedisConfigDto, RedisCommandDto
from model.address import PityGateway
from model.database import PityDatabase
from model.redis_config import PityRedis
from model.sql_log import PitySQLHistory
from proto.config_pb2 import ListGatewayResponseDto, GatewayResponseDto, Response, PityGatewayModel, \
    ListDbConfigResponseDto, PityDatabaseModel, ListEnvironmentResponseDto, \
    UpdateEnvironmentResponseDto, Environment, ListGConfigResponseDto, GConfigModelData, GConfigModel, \
    ListRedisResponseDto, PityRedisModel, RedisResponseDto, CommandResponse, ListTableResponseDto, TableResponse, \
    ListDatabaseResponseDto, DbTree, RunSQLResponseDto, SqlResult, QuerySQLHistoryResponseDto, SQLHistoryResponse
from proto.config_pb2_grpc import configServicer
from model.environment import Environment as Env


class ConfigServiceApi(configServicer):
    @Interceptor(PityGatewayDto, ListGatewayResponseDto)
    async def listGateway(self, request, context):
        data = await PityGatewayDao.select_list(env=request.env or None,
                                                gateway=f"%{request.gateway}%",
                                                name=f"%{request.name}%")
        return PityResponse.from_orm_list(data, PityGatewayModel)

    @Interceptor(PityAddressForm, GatewayResponseDto, role=Config.MANAGER)
    async def insertGateway(self, request, context):
        user = Context.get_user(context)
        model = PityGateway(user_id=user.id, **request.dict())
        model = await PityGatewayDao.insert(model=model, log=True)
        return PityResponse.from_orm(model, PityGatewayModel())

    @Interceptor(PityAddressForm, GatewayResponseDto, role=Config.MANAGER)
    async def updateGateway(self, request, context):
        user = Context.get_user(context)
        model = await PityGatewayDao.update_record_by_id(user.id, request, True, log=True)
        return PityResponse.from_orm(model, PityGatewayModel())

    @Interceptor(CustomDto, Response, role=Config.MANAGER)
    async def deleteGateway(self, request, context):
        user = Context.get_user(context)
        async with async_session() as session:
            await PityGatewayDao.delete_record_by_id(session, user.id, request.id)

    @Interceptor(QueryDatabaseDto, ListDbConfigResponseDto)
    async def listDbConfig(self, request, context):
        """获取数据库配置
        """
        data = await DbConfigDao.list_database(**request.dict())
        return PityResponse.from_orm_list(data, PityDatabaseModel)

    @Interceptor(DatabaseDto, Response, role=Config.ADMIN)
    async def insertDbConfig(self, request, context):
        """
        添加数据库配置
        """
        user = Context.get_user(context)
        await DbConfigDao.insert_database(request, user.id)

    @Interceptor(DatabaseDto, Response, role=Config.ADMIN)
    async def updateDbConfig(self, request, context):
        """
        编辑数据库配置
        """
        user = Context.get_user(context)
        await DbConfigDao.update_database(request, user.id)

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteDbConfig(self, request, context):
        """
        删除数据库配置
        """
        user = Context.get_user(context)
        await DbConfigDao.delete_database(request.id, user.id)

    @Interceptor(TestDatabaseDto, Response)
    async def testDbConfig(self, request, context):
        """
        测试数据库连接
        """
        data = await db_helper.get_connection(**request.dict())
        if data is None:
            raise Exception("测试连接失败")
        await DatabaseHelper.test_connection(data.get("session"))

    @Interceptor(None, ListDatabaseResponseDto)
    async def listDbTree(self, request, context):
        """
        获取db树
        """
        result = await DbConfigDao.query_database_tree()
        return Context.render_list(result, DbTree, "deleted_at")

    @Interceptor(DatabaseDto, ListTableResponseDto)
    async def listDbTables(self, request, context):
        """
        获取数据库表结构
        """
        children, tables = await DbConfigDao.get_tables(request)
        return Context.render(dict(children=children, tables=list(tables)), TableResponse)

    @Interceptor(RunSQLCommandDto, RunSQLResponseDto)
    async def runSQL(self, request, context):
        """
        在线执行SQL语句
        """
        user = Context.get_user(context)
        result, elapsed = await DbConfigDao.online_sql(request.id, request.sql)
        columns, result = PityResponse.parse_sql_result(result)
        await PitySQLHistoryDao.insert(model=PitySQLHistory(request.sql, elapsed, request.id, user.id))
        return Context.render(dict(result=result, columns=columns, elapsed=elapsed), SqlResult)

    @Interceptor(QuerySQLHistoryDto, QuerySQLHistoryResponseDto)
    async def querySQLHistory(self, request, context):
        """
        查询sql执行历史记录
        """
        data, total = await PitySQLHistoryDao.list_with_pagination(request.page, request.size,
                                                                   _sort=[PitySQLHistory.created_at.desc()],
                                                                   _select=[PityDatabase, Env],
                                                                   _join=[(PityDatabase,
                                                                           PityDatabase.id == PitySQLHistory.database_id),
                                                                          (Env, Env.id == PityDatabase.env)
                                                                          ])
        ans = []
        for history, database, env in data:
            database.env_info = env
            history.database = database
            ans.append(history)
        data = PityResponse.encode_json(ans, "deleted_at")
        return Context.render(dict(data=data, total=total), SQLHistoryResponse)

    @Interceptor(QueryEnvironmentDto, ListEnvironmentResponseDto)
    async def listEnvironment(self, request, context):
        """
        获取环境列表
        """
        data = await EnvironmentDao.list_env()
        return PityResponse.from_orm_list(data, Environment)

    @Interceptor(EnvironmentDto, Response, role=Config.ADMIN)
    async def insertEnvironment(self, request, context):
        """
        插入环境
        """
        user = Context.get_user(context)
        await EnvironmentDao.insert_env(request, user.id)

    @Interceptor(EnvironmentDto, UpdateEnvironmentResponseDto, role=Config.ADMIN)
    async def updateEnvironment(self, request, context):
        """
        修改环境
        """
        user = Context.get_user(context)
        ans = await EnvironmentDao.update_record_by_id(user.id, request, True, True)
        return PityResponse.from_orm(ans, Environment())

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteEnvironment(self, request, context):
        """
        删除环境
        """
        user = Context.get_user(context)
        async with async_session() as session:
            await EnvironmentDao.delete_record_by_id(session, user.id, request.id)

    @Interceptor(QueryGConfigDto, ListGConfigResponseDto)
    async def listGConfig(self, request, context):
        """
        获取全局变量
        """
        data, total = await GConfigDao.list_with_pagination(
            request.page, request.size, env=None if request.env == 0 else request.env, key=request.key)
        return GConfigModelData(data=PityResponse.from_orm_list(data, GConfigModel), total=total)

    @Interceptor(GConfigDto, Response, role=Config.ADMIN)
    async def insertGConfig(self, request, context):
        """
        添加全局变量
        """
        user = Context.get_user(context)
        await GConfigDao.insert_gconfig(request, user.id)

    @Interceptor(GConfigDto, Response, role=Config.ADMIN)
    async def updateGConfig(self, request, context):
        """
        修改全局变量
        """
        user = Context.get_user(context)
        await GConfigDao.update_record_by_id(user.id, request, True, True)

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteGConfig(self, request, context):
        """
        删除全局变量
        """
        user = Context.get_user(context)
        async with async_session() as session:
            await GConfigDao.delete_record_by_id(session, user.id, request.id, log=True)

    @Interceptor(QueryRedisDto, ListRedisResponseDto)
    async def listRedis(self, request, context):
        """
        获取redis配置
        """
        data = await PityRedisConfigDao.select_list(
            name=PityRedisConfigDao.like(request.name), addr=PityRedisConfigDao.like(request.addr),
            env=request.env if request.env != 0 else None, cluster=request.cluster
        )
        return PityResponse.from_orm_list(data, PityRedisModel)

    @Interceptor(RedisConfigDto, RedisResponseDto, role=Config.ADMIN)
    async def insertRedis(self, request, context):
        """
        添加redis配置
        """
        user = Context.get_user(context)
        query = await PityRedisConfigDao.query_record(name=request.name, env=request.env)
        if query is not None:
            raise Exception("数据已存在, 请勿重复添加")
        data = PityRedis(user_id=user.id, **request.dict())
        result = await PityRedisConfigDao.insert(model=data, log=True)
        return PityResponse.from_orm(result, PityRedisModel())

    @Interceptor(RedisConfigDto, RedisResponseDto, role=Config.ADMIN)
    async def updateRedis(self, request, context):
        """
        修改redis配置
        """
        user = Context.get_user(context)
        result = await PityRedisConfigDao.update_record_by_id(user.id, request, log=True)
        return PityResponse.from_orm(result, PityRedisModel())

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteRedis(self, request, context):
        """
        修改redis配置
        """
        user = Context.get_user(context)
        async with async_session() as session:
            ans = await PityRedisConfigDao.delete_record_by_id(session, user.id, request.id)
            # 更新缓存
            PityRedisManager.delete_client(request.id, ans.cluster)

    @Interceptor(RedisCommandDto, CommandResponse)
    async def runRedisCommand(self, request, context):
        """
        在线执行redis命令
        """
        ans = await PityRedisConfigDao.execute_command(request.command, id=request.id)
        return json.dumps(ans, ensure_ascii=False)
