# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63onfig.proto\x1a\x1cgoogle/protobuf/struct.proto\"\t\n\x07Request\"3\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\":\n\x0f\x43ommandResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\t\"\x9c\x01\n\x10PityGatewayModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0b\n\x03\x65nv\x18\x07 \x01(\x05\x12\x0f\n\x07gateway\x18\x08 \x01(\t\"h\n\x0eListGatewayDto\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x14\n\x07gateway\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03\x65nv\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\x07\n\x05_nameB\n\n\x08_gatewayB\x06\n\x04_env\"T\n\x16ListGatewayResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x1f\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x11.PityGatewayModel\x12\x0b\n\x03msg\x18\x03 \x01(\t\"P\n\x12GatewayResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x1f\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x11.PityGatewayModel\x12\x0b\n\x03msg\x18\x03 \x01(\t\"T\n\x0ePityGatewayDto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0b\n\x03\x65nv\x18\x02 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07gateway\x18\x04 \x01(\tB\x05\n\x03_id\"\x17\n\tCustomDto\x12\n\n\x02id\x18\x01 \x01(\x05\"1\n\x12RunRedisCommandDto\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ommand\x18\x02 \x01(\t\"l\n\x10QueryDbConfigDto\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x08\x64\x61tabase\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x10\n\x03\x65nv\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\x07\n\x05_nameB\x0b\n\t_databaseB\x06\n\x04_env\"\x90\x02\n\x11PityDatabaseModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0b\n\x03\x65nv\x18\x06 \x01(\x05\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0c\n\x04host\x18\x08 \x01(\t\x12\x0c\n\x04port\x18\t \x01(\x05\x12\x10\n\x08username\x18\n \x01(\t\x12\x10\n\x08password\x18\x0b \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x0c \x01(\t\x12\x10\n\x08sql_type\x18\r \x01(\x05\x12\x1e\n\x08\x65nv_info\x18\x0e \x01(\x0b\x32\x0c.Environment\"\x8a\x01\n\x0b\x45nvironment\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0f\n\x07remarks\x18\x07 \x01(\t\"V\n\x17ListDbConfigResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12 \n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x12.PityDatabaseModel\"\xc9\x01\n\x10\x44\x61tabaseModelDto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04host\x18\x03 \x01(\t\x12\x11\n\x04port\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x10\n\x08username\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x07 \x01(\t\x12\x15\n\x08sql_type\x18\x08 \x01(\x05H\x02\x88\x01\x01\x12\x0b\n\x03\x65nv\x18\t \x01(\x05\x42\x05\n\x03_idB\x07\n\x05_portB\x0b\n\t_sql_type\"\x8d\x01\n\x15\x44\x61tabaseConnectionDto\x12\x15\n\x08sql_type\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x10\n\x08password\x18\x05 \x01(\t\x12\x10\n\x08\x64\x61tabase\x18\x06 \x01(\tB\x0b\n\t_sql_type\"0\n\x12ListEnvironmentDto\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"S\n\x1aListEnvironmentResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x1a\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x0c.Environment\"L\n\x13\x45nvironmentModelDto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07remarks\x18\x03 \x01(\tB\x05\n\x03_id\"U\n\x1cUpdateEnvironmentResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x1a\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0c.Environment\"|\n\x0eListGConfigDto\x12\x11\n\x04page\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04size\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x10\n\x03\x65nv\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x10\n\x03key\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_pageB\x07\n\x05_sizeB\x06\n\x04_envB\x06\n\x04_key\"\xd9\x01\n\x0cGConfigModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0b\n\x03\x65nv\x18\x06 \x01(\x05\x12\x0b\n\x03key\x18\x07 \x01(\t\x12\r\n\x05value\x18\x08 \x01(\t\x12\x15\n\x08key_type\x18\t \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06\x65nable\x18\n \x01(\x08H\x01\x88\x01\x01\x42\x0b\n\t_key_typeB\t\n\x07_enable\">\n\x10GConfigModelData\x12\x1b\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\r.GConfigModel\x12\r\n\x05total\x18\x02 \x01(\x05\"T\n\x16ListGConfigResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x1f\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x11.GConfigModelData\"\x9e\x01\n\nGConfigDto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x10\n\x03\x65nv\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08key_type\x18\x05 \x01(\x05H\x02\x88\x01\x01\x12\x13\n\x06\x65nable\x18\x06 \x01(\x08H\x03\x88\x01\x01\x42\x05\n\x03_idB\x06\n\x04_envB\x0b\n\t_key_typeB\t\n\x07_enable\"d\n\x0cListRedisDto\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04\x61\x64\x64r\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x0b\n\x03\x65nv\x18\x03 \x01(\x05\x12\x0f\n\x07\x63luster\x18\x04 \x01(\x08\x42\x07\n\x05_nameB\x07\n\x05_addr\"\xd8\x01\n\x0ePityRedisModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0b\n\x03\x65nv\x18\x06 \x01(\x05\x12\x0c\n\x04name\x18\x07 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x08 \x01(\t\x12\x10\n\x08username\x18\t \x01(\t\x12\x10\n\x08password\x18\n \x01(\t\x12\n\n\x02\x64\x62\x18\x0b \x01(\x05\x12\x0f\n\x07\x63luster\x18\x0c \x01(\x08\"P\n\x14ListRedisResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x1d\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x0f.PityRedisModel\"\xa9\x01\n\x08RedisDto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x61\x64\x64r\x18\x03 \x01(\t\x12\x0f\n\x02\x64\x62\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x15\n\x08password\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07\x63luster\x18\x06 \x01(\x08H\x03\x88\x01\x01\x12\x0b\n\x03\x65nv\x18\x07 \x01(\x05\x42\x05\n\x03_idB\x05\n\x03_dbB\x0b\n\t_passwordB\n\n\x08_cluster\"L\n\x10RedisResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x1d\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0f.PityRedisModel\"E\n\x06\x44\x62Tree\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x1f\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\r.DatabaseInfo\"\x7f\n\x0c\x44\x61tabaseInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12 \n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x12.PityDatabaseModel\x12\x10\n\x08sql_type\x18\x04 \x01(\x05\x12\x1f\n\x08\x63hildren\x18\x05 \x03(\x0b\x32\r.DatabaseInfo\"=\n\x05Table\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x18\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x06.Field\"\x89\x01\n\x05\x46ield\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x0bprimary_key\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12\x11\n\x04type\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x0b\n\x03key\x18\x04 \x01(\t\x12\x13\n\x06isLeaf\x18\x05 \x01(\x08H\x02\x88\x01\x01\x42\x0e\n\x0c_primary_keyB\x07\n\x05_typeB\t\n\x07_isLeaf\"O\n\x14ListTableResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x1c\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x0e.TableResponse\"K\n\x17ListDatabaseResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x15\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x07.DbTree\"9\n\rTableResponse\x12\x18\n\x08\x63hildren\x18\x01 \x03(\x0b\x32\x06.Table\x12\x0e\n\x06tables\x18\x02 \x03(\t\"(\n\rSqlCommandDto\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0b\n\x03sql\x18\x02 \x01(\t\"V\n\tSqlResult\x12\'\n\x06result\x18\x01 \x03(\x0b\x32\x17.google.protobuf.Struct\x12\x0f\n\x07\x65lapsed\x18\x02 \x01(\x05\x12\x0f\n\x07\x63olumns\x18\x03 \x03(\t\"H\n\x11RunSQLResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x18\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\n.SqlResult\"0\n\x12QuerySQLHistoryDto\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x0c\n\x04size\x18\x02 \x01(\x05\"Z\n\x1aQuerySQLHistoryResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12!\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x13.SQLHistoryResponse\"\xcc\x01\n\x13PitySQLHistoryModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0b\n\x03sql\x18\x06 \x01(\t\x12\x0f\n\x07\x65lapsed\x18\x07 \x01(\x05\x12\x13\n\x0b\x64\x61tabase_id\x18\x08 \x01(\x05\x12$\n\x08\x64\x61tabase\x18\t \x01(\x0b\x32\x12.PityDatabaseModel\"G\n\x12SQLHistoryResponse\x12\"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.PitySQLHistoryModel\x12\r\n\x05total\x18\x02 \x01(\x05\x32\xf4\n\n\x06\x63onfig\x12\x39\n\x0blistGateway\x12\x0f.ListGatewayDto\x1a\x17.ListGatewayResponseDto\"\x00\x12\x37\n\rinsertGateway\x12\x0f.PityGatewayDto\x1a\x13.GatewayResponseDto\"\x00\x12\x37\n\rupdateGateway\x12\x0f.PityGatewayDto\x1a\x13.GatewayResponseDto\"\x00\x12(\n\rdeleteGateway\x12\n.CustomDto\x1a\t.Response\"\x00\x12=\n\x0clistDbConfig\x12\x11.QueryDbConfigDto\x1a\x18.ListDbConfigResponseDto\"\x00\x12\x30\n\x0einsertDbConfig\x12\x11.DatabaseModelDto\x1a\t.Response\"\x00\x12\x30\n\x0eupdateDbConfig\x12\x11.DatabaseModelDto\x1a\t.Response\"\x00\x12)\n\x0e\x64\x65leteDbConfig\x12\n.CustomDto\x1a\t.Response\"\x00\x12\x33\n\x0ctestDbConfig\x12\x16.DatabaseConnectionDto\x1a\t.Response\"\x00\x12\x32\n\nlistDbTree\x12\x08.Request\x1a\x18.ListDatabaseResponseDto\"\x00\x12:\n\x0clistDbTables\x12\x11.DatabaseModelDto\x1a\x15.ListTableResponseDto\"\x00\x12.\n\x06runSQL\x12\x0e.SqlCommandDto\x1a\x12.RunSQLResponseDto\"\x00\x12\x45\n\x0fquerySQLHistory\x12\x13.QuerySQLHistoryDto\x1a\x1b.QuerySQLHistoryResponseDto\"\x00\x12\x45\n\x0flistEnvironment\x12\x13.ListEnvironmentDto\x1a\x1b.ListEnvironmentResponseDto\"\x00\x12\x36\n\x11insertEnvironment\x12\x14.EnvironmentModelDto\x1a\t.Response\"\x00\x12J\n\x11updateEnvironment\x12\x14.EnvironmentModelDto\x1a\x1d.UpdateEnvironmentResponseDto\"\x00\x12,\n\x11\x64\x65leteEnvironment\x12\n.CustomDto\x1a\t.Response\"\x00\x12\x39\n\x0blistGConfig\x12\x0f.ListGConfigDto\x1a\x17.ListGConfigResponseDto\"\x00\x12)\n\rinsertGConfig\x12\x0b.GConfigDto\x1a\t.Response\"\x00\x12)\n\rupdateGConfig\x12\x0b.GConfigDto\x1a\t.Response\"\x00\x12(\n\rdeleteGConfig\x12\n.CustomDto\x1a\t.Response\"\x00\x12\x33\n\tlistRedis\x12\r.ListRedisDto\x1a\x15.ListRedisResponseDto\"\x00\x12-\n\x0binsertRedis\x12\t.RedisDto\x1a\x11.RedisResponseDto\"\x00\x12-\n\x0bupdateRedis\x12\t.RedisDto\x1a\x11.RedisResponseDto\"\x00\x12&\n\x0b\x64\x65leteRedis\x12\n.CustomDto\x1a\t.Response\"\x00\x12:\n\x0frunRedisCommand\x12\x13.RunRedisCommandDto\x1a\x10.CommandResponse\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_RESPONSE = DESCRIPTOR.message_types_by_name['Response']
_COMMANDRESPONSE = DESCRIPTOR.message_types_by_name['CommandResponse']
_PITYGATEWAYMODEL = DESCRIPTOR.message_types_by_name['PityGatewayModel']
_LISTGATEWAYDTO = DESCRIPTOR.message_types_by_name['ListGatewayDto']
_LISTGATEWAYRESPONSEDTO = DESCRIPTOR.message_types_by_name['ListGatewayResponseDto']
_GATEWAYRESPONSEDTO = DESCRIPTOR.message_types_by_name['GatewayResponseDto']
_PITYGATEWAYDTO = DESCRIPTOR.message_types_by_name['PityGatewayDto']
_CUSTOMDTO = DESCRIPTOR.message_types_by_name['CustomDto']
_RUNREDISCOMMANDDTO = DESCRIPTOR.message_types_by_name['RunRedisCommandDto']
_QUERYDBCONFIGDTO = DESCRIPTOR.message_types_by_name['QueryDbConfigDto']
_PITYDATABASEMODEL = DESCRIPTOR.message_types_by_name['PityDatabaseModel']
_ENVIRONMENT = DESCRIPTOR.message_types_by_name['Environment']
_LISTDBCONFIGRESPONSEDTO = DESCRIPTOR.message_types_by_name['ListDbConfigResponseDto']
_DATABASEMODELDTO = DESCRIPTOR.message_types_by_name['DatabaseModelDto']
_DATABASECONNECTIONDTO = DESCRIPTOR.message_types_by_name['DatabaseConnectionDto']
_LISTENVIRONMENTDTO = DESCRIPTOR.message_types_by_name['ListEnvironmentDto']
_LISTENVIRONMENTRESPONSEDTO = DESCRIPTOR.message_types_by_name['ListEnvironmentResponseDto']
_ENVIRONMENTMODELDTO = DESCRIPTOR.message_types_by_name['EnvironmentModelDto']
_UPDATEENVIRONMENTRESPONSEDTO = DESCRIPTOR.message_types_by_name['UpdateEnvironmentResponseDto']
_LISTGCONFIGDTO = DESCRIPTOR.message_types_by_name['ListGConfigDto']
_GCONFIGMODEL = DESCRIPTOR.message_types_by_name['GConfigModel']
_GCONFIGMODELDATA = DESCRIPTOR.message_types_by_name['GConfigModelData']
_LISTGCONFIGRESPONSEDTO = DESCRIPTOR.message_types_by_name['ListGConfigResponseDto']
_GCONFIGDTO = DESCRIPTOR.message_types_by_name['GConfigDto']
_LISTREDISDTO = DESCRIPTOR.message_types_by_name['ListRedisDto']
_PITYREDISMODEL = DESCRIPTOR.message_types_by_name['PityRedisModel']
_LISTREDISRESPONSEDTO = DESCRIPTOR.message_types_by_name['ListRedisResponseDto']
_REDISDTO = DESCRIPTOR.message_types_by_name['RedisDto']
_REDISRESPONSEDTO = DESCRIPTOR.message_types_by_name['RedisResponseDto']
_DBTREE = DESCRIPTOR.message_types_by_name['DbTree']
_DATABASEINFO = DESCRIPTOR.message_types_by_name['DatabaseInfo']
_TABLE = DESCRIPTOR.message_types_by_name['Table']
_FIELD = DESCRIPTOR.message_types_by_name['Field']
_LISTTABLERESPONSEDTO = DESCRIPTOR.message_types_by_name['ListTableResponseDto']
_LISTDATABASERESPONSEDTO = DESCRIPTOR.message_types_by_name['ListDatabaseResponseDto']
_TABLERESPONSE = DESCRIPTOR.message_types_by_name['TableResponse']
_SQLCOMMANDDTO = DESCRIPTOR.message_types_by_name['SqlCommandDto']
_SQLRESULT = DESCRIPTOR.message_types_by_name['SqlResult']
_RUNSQLRESPONSEDTO = DESCRIPTOR.message_types_by_name['RunSQLResponseDto']
_QUERYSQLHISTORYDTO = DESCRIPTOR.message_types_by_name['QuerySQLHistoryDto']
_QUERYSQLHISTORYRESPONSEDTO = DESCRIPTOR.message_types_by_name['QuerySQLHistoryResponseDto']
_PITYSQLHISTORYMODEL = DESCRIPTOR.message_types_by_name['PitySQLHistoryModel']
_SQLHISTORYRESPONSE = DESCRIPTOR.message_types_by_name['SQLHistoryResponse']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Response)
  })
_sym_db.RegisterMessage(Response)

CommandResponse = _reflection.GeneratedProtocolMessageType('CommandResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDRESPONSE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:CommandResponse)
  })
_sym_db.RegisterMessage(CommandResponse)

PityGatewayModel = _reflection.GeneratedProtocolMessageType('PityGatewayModel', (_message.Message,), {
  'DESCRIPTOR' : _PITYGATEWAYMODEL,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:PityGatewayModel)
  })
_sym_db.RegisterMessage(PityGatewayModel)

ListGatewayDto = _reflection.GeneratedProtocolMessageType('ListGatewayDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTGATEWAYDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListGatewayDto)
  })
_sym_db.RegisterMessage(ListGatewayDto)

ListGatewayResponseDto = _reflection.GeneratedProtocolMessageType('ListGatewayResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTGATEWAYRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListGatewayResponseDto)
  })
_sym_db.RegisterMessage(ListGatewayResponseDto)

GatewayResponseDto = _reflection.GeneratedProtocolMessageType('GatewayResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAYRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:GatewayResponseDto)
  })
_sym_db.RegisterMessage(GatewayResponseDto)

PityGatewayDto = _reflection.GeneratedProtocolMessageType('PityGatewayDto', (_message.Message,), {
  'DESCRIPTOR' : _PITYGATEWAYDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:PityGatewayDto)
  })
_sym_db.RegisterMessage(PityGatewayDto)

CustomDto = _reflection.GeneratedProtocolMessageType('CustomDto', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:CustomDto)
  })
_sym_db.RegisterMessage(CustomDto)

RunRedisCommandDto = _reflection.GeneratedProtocolMessageType('RunRedisCommandDto', (_message.Message,), {
  'DESCRIPTOR' : _RUNREDISCOMMANDDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:RunRedisCommandDto)
  })
_sym_db.RegisterMessage(RunRedisCommandDto)

QueryDbConfigDto = _reflection.GeneratedProtocolMessageType('QueryDbConfigDto', (_message.Message,), {
  'DESCRIPTOR' : _QUERYDBCONFIGDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:QueryDbConfigDto)
  })
_sym_db.RegisterMessage(QueryDbConfigDto)

PityDatabaseModel = _reflection.GeneratedProtocolMessageType('PityDatabaseModel', (_message.Message,), {
  'DESCRIPTOR' : _PITYDATABASEMODEL,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:PityDatabaseModel)
  })
_sym_db.RegisterMessage(PityDatabaseModel)

Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENT,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Environment)
  })
_sym_db.RegisterMessage(Environment)

ListDbConfigResponseDto = _reflection.GeneratedProtocolMessageType('ListDbConfigResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTDBCONFIGRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListDbConfigResponseDto)
  })
_sym_db.RegisterMessage(ListDbConfigResponseDto)

DatabaseModelDto = _reflection.GeneratedProtocolMessageType('DatabaseModelDto', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEMODELDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:DatabaseModelDto)
  })
_sym_db.RegisterMessage(DatabaseModelDto)

DatabaseConnectionDto = _reflection.GeneratedProtocolMessageType('DatabaseConnectionDto', (_message.Message,), {
  'DESCRIPTOR' : _DATABASECONNECTIONDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:DatabaseConnectionDto)
  })
_sym_db.RegisterMessage(DatabaseConnectionDto)

ListEnvironmentDto = _reflection.GeneratedProtocolMessageType('ListEnvironmentDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTENVIRONMENTDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListEnvironmentDto)
  })
_sym_db.RegisterMessage(ListEnvironmentDto)

ListEnvironmentResponseDto = _reflection.GeneratedProtocolMessageType('ListEnvironmentResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTENVIRONMENTRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListEnvironmentResponseDto)
  })
_sym_db.RegisterMessage(ListEnvironmentResponseDto)

EnvironmentModelDto = _reflection.GeneratedProtocolMessageType('EnvironmentModelDto', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENTMODELDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:EnvironmentModelDto)
  })
_sym_db.RegisterMessage(EnvironmentModelDto)

UpdateEnvironmentResponseDto = _reflection.GeneratedProtocolMessageType('UpdateEnvironmentResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEENVIRONMENTRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:UpdateEnvironmentResponseDto)
  })
_sym_db.RegisterMessage(UpdateEnvironmentResponseDto)

ListGConfigDto = _reflection.GeneratedProtocolMessageType('ListGConfigDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTGCONFIGDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListGConfigDto)
  })
_sym_db.RegisterMessage(ListGConfigDto)

GConfigModel = _reflection.GeneratedProtocolMessageType('GConfigModel', (_message.Message,), {
  'DESCRIPTOR' : _GCONFIGMODEL,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:GConfigModel)
  })
_sym_db.RegisterMessage(GConfigModel)

GConfigModelData = _reflection.GeneratedProtocolMessageType('GConfigModelData', (_message.Message,), {
  'DESCRIPTOR' : _GCONFIGMODELDATA,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:GConfigModelData)
  })
_sym_db.RegisterMessage(GConfigModelData)

ListGConfigResponseDto = _reflection.GeneratedProtocolMessageType('ListGConfigResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTGCONFIGRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListGConfigResponseDto)
  })
_sym_db.RegisterMessage(ListGConfigResponseDto)

GConfigDto = _reflection.GeneratedProtocolMessageType('GConfigDto', (_message.Message,), {
  'DESCRIPTOR' : _GCONFIGDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:GConfigDto)
  })
_sym_db.RegisterMessage(GConfigDto)

ListRedisDto = _reflection.GeneratedProtocolMessageType('ListRedisDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTREDISDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListRedisDto)
  })
_sym_db.RegisterMessage(ListRedisDto)

PityRedisModel = _reflection.GeneratedProtocolMessageType('PityRedisModel', (_message.Message,), {
  'DESCRIPTOR' : _PITYREDISMODEL,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:PityRedisModel)
  })
_sym_db.RegisterMessage(PityRedisModel)

ListRedisResponseDto = _reflection.GeneratedProtocolMessageType('ListRedisResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTREDISRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListRedisResponseDto)
  })
_sym_db.RegisterMessage(ListRedisResponseDto)

RedisDto = _reflection.GeneratedProtocolMessageType('RedisDto', (_message.Message,), {
  'DESCRIPTOR' : _REDISDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:RedisDto)
  })
_sym_db.RegisterMessage(RedisDto)

RedisResponseDto = _reflection.GeneratedProtocolMessageType('RedisResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _REDISRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:RedisResponseDto)
  })
_sym_db.RegisterMessage(RedisResponseDto)

DbTree = _reflection.GeneratedProtocolMessageType('DbTree', (_message.Message,), {
  'DESCRIPTOR' : _DBTREE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:DbTree)
  })
_sym_db.RegisterMessage(DbTree)

DatabaseInfo = _reflection.GeneratedProtocolMessageType('DatabaseInfo', (_message.Message,), {
  'DESCRIPTOR' : _DATABASEINFO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:DatabaseInfo)
  })
_sym_db.RegisterMessage(DatabaseInfo)

Table = _reflection.GeneratedProtocolMessageType('Table', (_message.Message,), {
  'DESCRIPTOR' : _TABLE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Table)
  })
_sym_db.RegisterMessage(Table)

Field = _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
  'DESCRIPTOR' : _FIELD,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:Field)
  })
_sym_db.RegisterMessage(Field)

ListTableResponseDto = _reflection.GeneratedProtocolMessageType('ListTableResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTTABLERESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListTableResponseDto)
  })
_sym_db.RegisterMessage(ListTableResponseDto)

ListDatabaseResponseDto = _reflection.GeneratedProtocolMessageType('ListDatabaseResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTDATABASERESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:ListDatabaseResponseDto)
  })
_sym_db.RegisterMessage(ListDatabaseResponseDto)

TableResponse = _reflection.GeneratedProtocolMessageType('TableResponse', (_message.Message,), {
  'DESCRIPTOR' : _TABLERESPONSE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:TableResponse)
  })
_sym_db.RegisterMessage(TableResponse)

SqlCommandDto = _reflection.GeneratedProtocolMessageType('SqlCommandDto', (_message.Message,), {
  'DESCRIPTOR' : _SQLCOMMANDDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:SqlCommandDto)
  })
_sym_db.RegisterMessage(SqlCommandDto)

SqlResult = _reflection.GeneratedProtocolMessageType('SqlResult', (_message.Message,), {
  'DESCRIPTOR' : _SQLRESULT,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:SqlResult)
  })
_sym_db.RegisterMessage(SqlResult)

RunSQLResponseDto = _reflection.GeneratedProtocolMessageType('RunSQLResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _RUNSQLRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:RunSQLResponseDto)
  })
_sym_db.RegisterMessage(RunSQLResponseDto)

QuerySQLHistoryDto = _reflection.GeneratedProtocolMessageType('QuerySQLHistoryDto', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSQLHISTORYDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:QuerySQLHistoryDto)
  })
_sym_db.RegisterMessage(QuerySQLHistoryDto)

QuerySQLHistoryResponseDto = _reflection.GeneratedProtocolMessageType('QuerySQLHistoryResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _QUERYSQLHISTORYRESPONSEDTO,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:QuerySQLHistoryResponseDto)
  })
_sym_db.RegisterMessage(QuerySQLHistoryResponseDto)

PitySQLHistoryModel = _reflection.GeneratedProtocolMessageType('PitySQLHistoryModel', (_message.Message,), {
  'DESCRIPTOR' : _PITYSQLHISTORYMODEL,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:PitySQLHistoryModel)
  })
_sym_db.RegisterMessage(PitySQLHistoryModel)

SQLHistoryResponse = _reflection.GeneratedProtocolMessageType('SQLHistoryResponse', (_message.Message,), {
  'DESCRIPTOR' : _SQLHISTORYRESPONSE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:SQLHistoryResponse)
  })
_sym_db.RegisterMessage(SQLHistoryResponse)

_CONFIG = DESCRIPTOR.services_by_name['config']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=46
  _REQUEST._serialized_end=55
  _RESPONSE._serialized_start=57
  _RESPONSE._serialized_end=108
  _COMMANDRESPONSE._serialized_start=110
  _COMMANDRESPONSE._serialized_end=168
  _PITYGATEWAYMODEL._serialized_start=171
  _PITYGATEWAYMODEL._serialized_end=327
  _LISTGATEWAYDTO._serialized_start=329
  _LISTGATEWAYDTO._serialized_end=433
  _LISTGATEWAYRESPONSEDTO._serialized_start=435
  _LISTGATEWAYRESPONSEDTO._serialized_end=519
  _GATEWAYRESPONSEDTO._serialized_start=521
  _GATEWAYRESPONSEDTO._serialized_end=601
  _PITYGATEWAYDTO._serialized_start=603
  _PITYGATEWAYDTO._serialized_end=687
  _CUSTOMDTO._serialized_start=689
  _CUSTOMDTO._serialized_end=712
  _RUNREDISCOMMANDDTO._serialized_start=714
  _RUNREDISCOMMANDDTO._serialized_end=763
  _QUERYDBCONFIGDTO._serialized_start=765
  _QUERYDBCONFIGDTO._serialized_end=873
  _PITYDATABASEMODEL._serialized_start=876
  _PITYDATABASEMODEL._serialized_end=1148
  _ENVIRONMENT._serialized_start=1151
  _ENVIRONMENT._serialized_end=1289
  _LISTDBCONFIGRESPONSEDTO._serialized_start=1291
  _LISTDBCONFIGRESPONSEDTO._serialized_end=1377
  _DATABASEMODELDTO._serialized_start=1380
  _DATABASEMODELDTO._serialized_end=1581
  _DATABASECONNECTIONDTO._serialized_start=1584
  _DATABASECONNECTIONDTO._serialized_end=1725
  _LISTENVIRONMENTDTO._serialized_start=1727
  _LISTENVIRONMENTDTO._serialized_end=1775
  _LISTENVIRONMENTRESPONSEDTO._serialized_start=1777
  _LISTENVIRONMENTRESPONSEDTO._serialized_end=1860
  _ENVIRONMENTMODELDTO._serialized_start=1862
  _ENVIRONMENTMODELDTO._serialized_end=1938
  _UPDATEENVIRONMENTRESPONSEDTO._serialized_start=1940
  _UPDATEENVIRONMENTRESPONSEDTO._serialized_end=2025
  _LISTGCONFIGDTO._serialized_start=2027
  _LISTGCONFIGDTO._serialized_end=2151
  _GCONFIGMODEL._serialized_start=2154
  _GCONFIGMODEL._serialized_end=2371
  _GCONFIGMODELDATA._serialized_start=2373
  _GCONFIGMODELDATA._serialized_end=2435
  _LISTGCONFIGRESPONSEDTO._serialized_start=2437
  _LISTGCONFIGRESPONSEDTO._serialized_end=2521
  _GCONFIGDTO._serialized_start=2524
  _GCONFIGDTO._serialized_end=2682
  _LISTREDISDTO._serialized_start=2684
  _LISTREDISDTO._serialized_end=2784
  _PITYREDISMODEL._serialized_start=2787
  _PITYREDISMODEL._serialized_end=3003
  _LISTREDISRESPONSEDTO._serialized_start=3005
  _LISTREDISRESPONSEDTO._serialized_end=3085
  _REDISDTO._serialized_start=3088
  _REDISDTO._serialized_end=3257
  _REDISRESPONSEDTO._serialized_start=3259
  _REDISRESPONSEDTO._serialized_end=3335
  _DBTREE._serialized_start=3337
  _DBTREE._serialized_end=3406
  _DATABASEINFO._serialized_start=3408
  _DATABASEINFO._serialized_end=3535
  _TABLE._serialized_start=3537
  _TABLE._serialized_end=3598
  _FIELD._serialized_start=3601
  _FIELD._serialized_end=3738
  _LISTTABLERESPONSEDTO._serialized_start=3740
  _LISTTABLERESPONSEDTO._serialized_end=3819
  _LISTDATABASERESPONSEDTO._serialized_start=3821
  _LISTDATABASERESPONSEDTO._serialized_end=3896
  _TABLERESPONSE._serialized_start=3898
  _TABLERESPONSE._serialized_end=3955
  _SQLCOMMANDDTO._serialized_start=3957
  _SQLCOMMANDDTO._serialized_end=3997
  _SQLRESULT._serialized_start=3999
  _SQLRESULT._serialized_end=4085
  _RUNSQLRESPONSEDTO._serialized_start=4087
  _RUNSQLRESPONSEDTO._serialized_end=4159
  _QUERYSQLHISTORYDTO._serialized_start=4161
  _QUERYSQLHISTORYDTO._serialized_end=4209
  _QUERYSQLHISTORYRESPONSEDTO._serialized_start=4211
  _QUERYSQLHISTORYRESPONSEDTO._serialized_end=4301
  _PITYSQLHISTORYMODEL._serialized_start=4304
  _PITYSQLHISTORYMODEL._serialized_end=4508
  _SQLHISTORYRESPONSE._serialized_start=4510
  _SQLHISTORYRESPONSE._serialized_end=4581
  _CONFIG._serialized_start=4584
  _CONFIG._serialized_end=5980
# @@protoc_insertion_point(module_scope)