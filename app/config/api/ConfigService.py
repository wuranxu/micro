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
from dto.address import PityAddressForm, CustomDto, PityGatewayDto, QueryGatewayDto
from dto.database import QueryDatabaseDto, DatabaseDto, TestDatabaseDto, RunSQLCommandDto, QuerySQLHistoryDto, \
    ExecuteSQLDto
from dto.environment import EnvironmentDto, QueryEnvironmentDto
from dto.gconfig import QueryGConfigDto, GConfigDto
from dto.redis_config import QueryRedisDto, RedisConfigDto, RedisCommandDto, RedisCommandWithNameDto
from model.address import PityGateway
from model.database import PityDatabase
from model.environment import Environment as Env
from model.redis_config import PityRedis
from model.sql_log import PitySQLHistory
from proto.config_pb2 import ListGatewayResponseDto, GatewayResponseDto, ConfigResponse as Response, PityGatewayModel, \
    ListDbConfigResponseDto, PityDatabaseModel, ListEnvironmentResponseDto, \
    UpdateEnvironmentResponseDto, Environment, ListGConfigResponseDto, GConfigModelData, GConfigModel, \
    ListRedisResponseDto, PityRedisModel, RedisResponseDto, CommandResponse, ListTableResponseDto, TableResponse, \
    ListDatabaseResponseDto, DbTree, RunSQLResponseDto, SqlResult, QuerySQLHistoryResponseDto, SQLHistoryResponse, \
    QueryGConfigResponse, ConfigStringResponse, QueryEnvironmentResponse
from proto.config_pb2_grpc import configServicer


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

    @Interceptor(QueryGatewayDto, Response, role=Config.MANAGER)
    async def queryGateway(self, request: QueryGatewayDto, context):
        """
        ??????name env??????gateway
        """
        return await PityGatewayDao.query_gateway(request.env, request.name)

    @Interceptor(QueryDatabaseDto, ListDbConfigResponseDto)
    async def listDbConfig(self, request, context):
        """?????????????????????
        """
        data = await DbConfigDao.list_database(**request.dict())
        return PityResponse.from_orm_list(data, PityDatabaseModel)

    @Interceptor(DatabaseDto, Response, role=Config.ADMIN)
    async def insertDbConfig(self, request, context):
        """
        ?????????????????????
        """
        user = Context.get_user(context)
        await DbConfigDao.insert_database(request, user.id)

    @Interceptor(DatabaseDto, Response, role=Config.ADMIN)
    async def updateDbConfig(self, request, context):
        """
        ?????????????????????
        """
        user = Context.get_user(context)
        await DbConfigDao.update_database(request, user.id)

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteDbConfig(self, request, context):
        """
        ?????????????????????
        """
        user = Context.get_user(context)
        await DbConfigDao.delete_database(request.id, user.id)

    @Interceptor(TestDatabaseDto, Response)
    async def testDbConfig(self, request, context):
        """
        ?????????????????????
        """
        data = await db_helper.get_connection(**request.dict())
        if data is None:
            raise Exception("??????????????????")
        await DatabaseHelper.test_connection(data.get("session"))

    @Interceptor(None, ListDatabaseResponseDto)
    async def listDbTree(self, request, context):
        """
        ??????db???
        """
        result = await DbConfigDao.query_database_tree()
        return Context.render_list(result, DbTree, "deleted_at")

    @Interceptor(DatabaseDto, ListTableResponseDto)
    async def listDbTables(self, request, context):
        """
        ????????????????????????
        """
        children, tables = await DbConfigDao.get_tables(request)
        return Context.render(dict(children=children, tables=list(tables)), TableResponse)

    @Interceptor(RunSQLCommandDto, RunSQLResponseDto)
    async def runSQL(self, request, context):
        """
        ????????????SQL??????
        """
        user = Context.get_user(context)
        result, elapsed = await DbConfigDao.online_sql(request.id, request.sql)
        columns, result = PityResponse.parse_sql_result(result)
        await PitySQLHistoryDao.insert(model=PitySQLHistory(request.sql, elapsed, request.id, user.id))
        return Context.render(dict(result=result, columns=columns, elapsed=elapsed), SqlResult)

    @Interceptor(ExecuteSQLDto, ConfigStringResponse)
    async def executeSQL(self, request: ExecuteSQLDto, context):
        """
        ????????????SQL??????
        """
        return await DbConfigDao.execute_sql(request.env, request.name, request.sql)

    @Interceptor(QuerySQLHistoryDto, QuerySQLHistoryResponseDto)
    async def querySQLHistory(self, request, context):
        """
        ??????sql??????????????????
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

    @Interceptor(CustomDto, QueryEnvironmentResponse)
    async def queryEnvironment(self, request: CustomDto, context):
        result = await EnvironmentDao.query_env(request.id)
        return PityResponse.from_orm(result, Environment)

    @Interceptor(QueryEnvironmentDto, ListEnvironmentResponseDto)
    async def listEnvironment(self, request: QueryEnvironmentDto, context):
        """
        ??????????????????
        """
        data = await EnvironmentDao.list_env(request.name)
        return PityResponse.from_orm_list(data, Environment)

    @Interceptor(EnvironmentDto, Response, role=Config.ADMIN)
    async def insertEnvironment(self, request, context):
        """
        ????????????
        """
        user = Context.get_user(context)
        await EnvironmentDao.insert_env(request, user.id)

    @Interceptor(EnvironmentDto, UpdateEnvironmentResponseDto, role=Config.ADMIN)
    async def updateEnvironment(self, request, context):
        """
        ????????????
        """
        user = Context.get_user(context)
        ans = await EnvironmentDao.update_record_by_id(user.id, request, True, True)
        return PityResponse.from_orm(ans, Environment())

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteEnvironment(self, request, context):
        """
        ????????????
        """
        user = Context.get_user(context)
        async with async_session() as session:
            await EnvironmentDao.delete_record_by_id(session, user.id, request.id)

    @Interceptor(QueryGConfigDto, ListGConfigResponseDto)
    async def listGConfig(self, request, context):
        """
        ??????????????????
        """
        data, total = await GConfigDao.list_with_pagination(
            request.page, request.size, env=None if request.env == 0 else request.env, key=request.key)
        return GConfigModelData(data=PityResponse.from_orm_list(data, GConfigModel), total=total)

    @Interceptor(GConfigDto, Response, role=Config.ADMIN)
    async def insertGConfig(self, request, context):
        """
        ??????????????????
        """
        user = Context.get_user(context)
        await GConfigDao.insert_gconfig(request, user.id)

    @Interceptor(GConfigDto, Response, role=Config.ADMIN)
    async def updateGConfig(self, request, context):
        """
        ??????????????????
        """
        user = Context.get_user(context)
        await GConfigDao.update_record_by_id(user.id, request, True, True)

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteGConfig(self, request, context):
        """
        ??????????????????
        """
        user = Context.get_user(context)
        async with async_session() as session:
            await GConfigDao.delete_record_by_id(session, user.id, request.id, log=True)

    @Interceptor(QueryGConfigDto, QueryGConfigResponse)
    async def getGConfigByKey(self, request: QueryGConfigDto, context):
        """
        ??????key??????????????????
        """
        return await GConfigDao.get_gconfig_by_key(request.key, request.env)

    @Interceptor(QueryRedisDto, ListRedisResponseDto)
    async def listRedis(self, request, context):
        """
        ??????redis??????
        """
        data = await PityRedisConfigDao.select_list(
            name=PityRedisConfigDao.like(request.name), addr=PityRedisConfigDao.like(request.addr),
            env=request.env if request.env != 0 else None, cluster=request.cluster
        )
        return PityResponse.from_orm_list(data, PityRedisModel)

    @Interceptor(RedisConfigDto, RedisResponseDto, role=Config.ADMIN)
    async def insertRedis(self, request, context):
        """
        ??????redis??????
        """
        user = Context.get_user(context)
        query = await PityRedisConfigDao.query_record(name=request.name, env=request.env)
        if query is not None:
            raise Exception("???????????????, ??????????????????")
        data = PityRedis(user_id=user.id, **request.dict())
        result = await PityRedisConfigDao.insert(model=data, log=True)
        return PityResponse.from_orm(result, PityRedisModel())

    @Interceptor(RedisConfigDto, RedisResponseDto, role=Config.ADMIN)
    async def updateRedis(self, request, context):
        """
        ??????redis??????
        """
        user = Context.get_user(context)
        result = await PityRedisConfigDao.update_record_by_id(user.id, request, log=True)
        return PityResponse.from_orm(result, PityRedisModel())

    @Interceptor(CustomDto, Response, role=Config.ADMIN)
    async def deleteRedis(self, request, context):
        """
        ??????redis??????
        """
        user = Context.get_user(context)
        async with async_session() as session:
            ans = await PityRedisConfigDao.delete_record_by_id(session, user.id, request.id)
            # ????????????
            PityRedisManager.delete_client(request.id, ans.cluster)

    @Interceptor(RedisCommandDto, CommandResponse)
    async def runRedisCommand(self, request, context):
        """
        ????????????redis??????
        """
        ans = await PityRedisConfigDao.execute_command(request.command, id=request.id)
        return json.dumps(ans, ensure_ascii=False)

    @Interceptor(RedisCommandWithNameDto, CommandResponse)
    async def runRedisCommandWithName(self, request: RedisCommandWithNameDto, context):
        """
        ????????????redis?????? ?????????????????????
        """
        ans = await PityRedisConfigDao.execute_command(request.command, env=request.env, name=request.name)
        return json.dumps(ans, ensure_ascii=False)
