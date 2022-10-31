# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.config_pb2 as config__pb2


class configStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.listGateway = channel.unary_unary(
                '/config/listGateway',
                request_serializer=config__pb2.ListGatewayDto.SerializeToString,
                response_deserializer=config__pb2.ListGatewayResponseDto.FromString,
                )
        self.insertGateway = channel.unary_unary(
                '/config/insertGateway',
                request_serializer=config__pb2.PityGatewayDto.SerializeToString,
                response_deserializer=config__pb2.GatewayResponseDto.FromString,
                )
        self.updateGateway = channel.unary_unary(
                '/config/updateGateway',
                request_serializer=config__pb2.PityGatewayDto.SerializeToString,
                response_deserializer=config__pb2.GatewayResponseDto.FromString,
                )
        self.deleteGateway = channel.unary_unary(
                '/config/deleteGateway',
                request_serializer=config__pb2.CustomDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.listDbConfig = channel.unary_unary(
                '/config/listDbConfig',
                request_serializer=config__pb2.QueryDbConfigDto.SerializeToString,
                response_deserializer=config__pb2.ListDbConfigResponseDto.FromString,
                )
        self.insertDbConfig = channel.unary_unary(
                '/config/insertDbConfig',
                request_serializer=config__pb2.DatabaseModelDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.updateDbConfig = channel.unary_unary(
                '/config/updateDbConfig',
                request_serializer=config__pb2.DatabaseModelDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.deleteDbConfig = channel.unary_unary(
                '/config/deleteDbConfig',
                request_serializer=config__pb2.CustomDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.testDbConfig = channel.unary_unary(
                '/config/testDbConfig',
                request_serializer=config__pb2.DatabaseConnectionDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.listDbTree = channel.unary_unary(
                '/config/listDbTree',
                request_serializer=config__pb2.Request.SerializeToString,
                response_deserializer=config__pb2.ListDatabaseResponseDto.FromString,
                )
        self.listDbTables = channel.unary_unary(
                '/config/listDbTables',
                request_serializer=config__pb2.DatabaseModelDto.SerializeToString,
                response_deserializer=config__pb2.ListTableResponseDto.FromString,
                )
        self.runSQL = channel.unary_unary(
                '/config/runSQL',
                request_serializer=config__pb2.SqlCommandDto.SerializeToString,
                response_deserializer=config__pb2.RunSQLResponseDto.FromString,
                )
        self.querySQLHistory = channel.unary_unary(
                '/config/querySQLHistory',
                request_serializer=config__pb2.QuerySQLHistoryDto.SerializeToString,
                response_deserializer=config__pb2.QuerySQLHistoryResponseDto.FromString,
                )
        self.listEnvironment = channel.unary_unary(
                '/config/listEnvironment',
                request_serializer=config__pb2.ListEnvironmentDto.SerializeToString,
                response_deserializer=config__pb2.ListEnvironmentResponseDto.FromString,
                )
        self.insertEnvironment = channel.unary_unary(
                '/config/insertEnvironment',
                request_serializer=config__pb2.EnvironmentModelDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.updateEnvironment = channel.unary_unary(
                '/config/updateEnvironment',
                request_serializer=config__pb2.EnvironmentModelDto.SerializeToString,
                response_deserializer=config__pb2.UpdateEnvironmentResponseDto.FromString,
                )
        self.deleteEnvironment = channel.unary_unary(
                '/config/deleteEnvironment',
                request_serializer=config__pb2.CustomDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.listGConfig = channel.unary_unary(
                '/config/listGConfig',
                request_serializer=config__pb2.ListGConfigDto.SerializeToString,
                response_deserializer=config__pb2.ListGConfigResponseDto.FromString,
                )
        self.insertGConfig = channel.unary_unary(
                '/config/insertGConfig',
                request_serializer=config__pb2.GConfigDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.updateGConfig = channel.unary_unary(
                '/config/updateGConfig',
                request_serializer=config__pb2.GConfigDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.deleteGConfig = channel.unary_unary(
                '/config/deleteGConfig',
                request_serializer=config__pb2.CustomDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.listRedis = channel.unary_unary(
                '/config/listRedis',
                request_serializer=config__pb2.ListRedisDto.SerializeToString,
                response_deserializer=config__pb2.ListRedisResponseDto.FromString,
                )
        self.insertRedis = channel.unary_unary(
                '/config/insertRedis',
                request_serializer=config__pb2.RedisDto.SerializeToString,
                response_deserializer=config__pb2.RedisResponseDto.FromString,
                )
        self.updateRedis = channel.unary_unary(
                '/config/updateRedis',
                request_serializer=config__pb2.RedisDto.SerializeToString,
                response_deserializer=config__pb2.RedisResponseDto.FromString,
                )
        self.deleteRedis = channel.unary_unary(
                '/config/deleteRedis',
                request_serializer=config__pb2.CustomDto.SerializeToString,
                response_deserializer=config__pb2.Response.FromString,
                )
        self.runRedisCommand = channel.unary_unary(
                '/config/runRedisCommand',
                request_serializer=config__pb2.RunRedisCommandDto.SerializeToString,
                response_deserializer=config__pb2.CommandResponse.FromString,
                )


class configServicer(object):
    """Missing associated documentation comment in .proto file."""

    def listGateway(self, request, context):
        """查询网关地址
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insertGateway(self, request, context):
        """添加网关地址
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateGateway(self, request, context):
        """编辑网关地址
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteGateway(self, request, context):
        """删除网关地址
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listDbConfig(self, request, context):
        """获取数据库配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insertDbConfig(self, request, context):
        """添加数据库配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateDbConfig(self, request, context):
        """编辑数据库配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteDbConfig(self, request, context):
        """删除数据库配置
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def testDbConfig(self, request, context):
        """测试数据库链接
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listDbTree(self, request, context):
        """获取数据库列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listDbTables(self, request, context):
        """获取数据库表+字段
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def runSQL(self, request, context):
        """在线执行sql
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def querySQLHistory(self, request, context):
        """查询sql执行记录
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listEnvironment(self, request, context):
        """获取环境列表
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insertEnvironment(self, request, context):
        """添加环境
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateEnvironment(self, request, context):
        """编辑环境
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteEnvironment(self, request, context):
        """删除环境
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listGConfig(self, request, context):
        """获取全局变量
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insertGConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateGConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteGConfig(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def listRedis(self, request, context):
        """redis配置curd
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def insertRedis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def updateRedis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def deleteRedis(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def runRedisCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_configServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'listGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.listGateway,
                    request_deserializer=config__pb2.ListGatewayDto.FromString,
                    response_serializer=config__pb2.ListGatewayResponseDto.SerializeToString,
            ),
            'insertGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.insertGateway,
                    request_deserializer=config__pb2.PityGatewayDto.FromString,
                    response_serializer=config__pb2.GatewayResponseDto.SerializeToString,
            ),
            'updateGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.updateGateway,
                    request_deserializer=config__pb2.PityGatewayDto.FromString,
                    response_serializer=config__pb2.GatewayResponseDto.SerializeToString,
            ),
            'deleteGateway': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteGateway,
                    request_deserializer=config__pb2.CustomDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'listDbConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.listDbConfig,
                    request_deserializer=config__pb2.QueryDbConfigDto.FromString,
                    response_serializer=config__pb2.ListDbConfigResponseDto.SerializeToString,
            ),
            'insertDbConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.insertDbConfig,
                    request_deserializer=config__pb2.DatabaseModelDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'updateDbConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.updateDbConfig,
                    request_deserializer=config__pb2.DatabaseModelDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'deleteDbConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteDbConfig,
                    request_deserializer=config__pb2.CustomDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'testDbConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.testDbConfig,
                    request_deserializer=config__pb2.DatabaseConnectionDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'listDbTree': grpc.unary_unary_rpc_method_handler(
                    servicer.listDbTree,
                    request_deserializer=config__pb2.Request.FromString,
                    response_serializer=config__pb2.ListDatabaseResponseDto.SerializeToString,
            ),
            'listDbTables': grpc.unary_unary_rpc_method_handler(
                    servicer.listDbTables,
                    request_deserializer=config__pb2.DatabaseModelDto.FromString,
                    response_serializer=config__pb2.ListTableResponseDto.SerializeToString,
            ),
            'runSQL': grpc.unary_unary_rpc_method_handler(
                    servicer.runSQL,
                    request_deserializer=config__pb2.SqlCommandDto.FromString,
                    response_serializer=config__pb2.RunSQLResponseDto.SerializeToString,
            ),
            'querySQLHistory': grpc.unary_unary_rpc_method_handler(
                    servicer.querySQLHistory,
                    request_deserializer=config__pb2.QuerySQLHistoryDto.FromString,
                    response_serializer=config__pb2.QuerySQLHistoryResponseDto.SerializeToString,
            ),
            'listEnvironment': grpc.unary_unary_rpc_method_handler(
                    servicer.listEnvironment,
                    request_deserializer=config__pb2.ListEnvironmentDto.FromString,
                    response_serializer=config__pb2.ListEnvironmentResponseDto.SerializeToString,
            ),
            'insertEnvironment': grpc.unary_unary_rpc_method_handler(
                    servicer.insertEnvironment,
                    request_deserializer=config__pb2.EnvironmentModelDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'updateEnvironment': grpc.unary_unary_rpc_method_handler(
                    servicer.updateEnvironment,
                    request_deserializer=config__pb2.EnvironmentModelDto.FromString,
                    response_serializer=config__pb2.UpdateEnvironmentResponseDto.SerializeToString,
            ),
            'deleteEnvironment': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteEnvironment,
                    request_deserializer=config__pb2.CustomDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'listGConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.listGConfig,
                    request_deserializer=config__pb2.ListGConfigDto.FromString,
                    response_serializer=config__pb2.ListGConfigResponseDto.SerializeToString,
            ),
            'insertGConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.insertGConfig,
                    request_deserializer=config__pb2.GConfigDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'updateGConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.updateGConfig,
                    request_deserializer=config__pb2.GConfigDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'deleteGConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteGConfig,
                    request_deserializer=config__pb2.CustomDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'listRedis': grpc.unary_unary_rpc_method_handler(
                    servicer.listRedis,
                    request_deserializer=config__pb2.ListRedisDto.FromString,
                    response_serializer=config__pb2.ListRedisResponseDto.SerializeToString,
            ),
            'insertRedis': grpc.unary_unary_rpc_method_handler(
                    servicer.insertRedis,
                    request_deserializer=config__pb2.RedisDto.FromString,
                    response_serializer=config__pb2.RedisResponseDto.SerializeToString,
            ),
            'updateRedis': grpc.unary_unary_rpc_method_handler(
                    servicer.updateRedis,
                    request_deserializer=config__pb2.RedisDto.FromString,
                    response_serializer=config__pb2.RedisResponseDto.SerializeToString,
            ),
            'deleteRedis': grpc.unary_unary_rpc_method_handler(
                    servicer.deleteRedis,
                    request_deserializer=config__pb2.CustomDto.FromString,
                    response_serializer=config__pb2.Response.SerializeToString,
            ),
            'runRedisCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.runRedisCommand,
                    request_deserializer=config__pb2.RunRedisCommandDto.FromString,
                    response_serializer=config__pb2.CommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'config', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class config(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def listGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listGateway',
            config__pb2.ListGatewayDto.SerializeToString,
            config__pb2.ListGatewayResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insertGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/insertGateway',
            config__pb2.PityGatewayDto.SerializeToString,
            config__pb2.GatewayResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/updateGateway',
            config__pb2.PityGatewayDto.SerializeToString,
            config__pb2.GatewayResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteGateway(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/deleteGateway',
            config__pb2.CustomDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listDbConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listDbConfig',
            config__pb2.QueryDbConfigDto.SerializeToString,
            config__pb2.ListDbConfigResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insertDbConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/insertDbConfig',
            config__pb2.DatabaseModelDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateDbConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/updateDbConfig',
            config__pb2.DatabaseModelDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteDbConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/deleteDbConfig',
            config__pb2.CustomDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def testDbConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/testDbConfig',
            config__pb2.DatabaseConnectionDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listDbTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listDbTree',
            config__pb2.Request.SerializeToString,
            config__pb2.ListDatabaseResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listDbTables(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listDbTables',
            config__pb2.DatabaseModelDto.SerializeToString,
            config__pb2.ListTableResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def runSQL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/runSQL',
            config__pb2.SqlCommandDto.SerializeToString,
            config__pb2.RunSQLResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def querySQLHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/querySQLHistory',
            config__pb2.QuerySQLHistoryDto.SerializeToString,
            config__pb2.QuerySQLHistoryResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listEnvironment',
            config__pb2.ListEnvironmentDto.SerializeToString,
            config__pb2.ListEnvironmentResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insertEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/insertEnvironment',
            config__pb2.EnvironmentModelDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/updateEnvironment',
            config__pb2.EnvironmentModelDto.SerializeToString,
            config__pb2.UpdateEnvironmentResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteEnvironment(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/deleteEnvironment',
            config__pb2.CustomDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listGConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listGConfig',
            config__pb2.ListGConfigDto.SerializeToString,
            config__pb2.ListGConfigResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insertGConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/insertGConfig',
            config__pb2.GConfigDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateGConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/updateGConfig',
            config__pb2.GConfigDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteGConfig(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/deleteGConfig',
            config__pb2.CustomDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def listRedis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/listRedis',
            config__pb2.ListRedisDto.SerializeToString,
            config__pb2.ListRedisResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def insertRedis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/insertRedis',
            config__pb2.RedisDto.SerializeToString,
            config__pb2.RedisResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def updateRedis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/updateRedis',
            config__pb2.RedisDto.SerializeToString,
            config__pb2.RedisResponseDto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def deleteRedis(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/deleteRedis',
            config__pb2.CustomDto.SerializeToString,
            config__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def runRedisCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/config/runRedisCommand',
            config__pb2.RunRedisCommandDto.SerializeToString,
            config__pb2.CommandResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)