# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rproject.proto\"%\n\x0eProjectRequest\x12\x13\n\x0brequestJson\x18\x01 \x01(\x0c\"\x13\n\x05Query\x12\n\n\x02id\x18\x01 \x01(\x05\":\n\x0fProjectResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"Z\n\rPermissionDto\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x16\n\tuser_role\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\nproject_id\x18\x03 \x01(\x05\x42\x0c\n\n_user_role\"@\n\x15PermissionResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x08\x12\x0b\n\x03msg\x18\x03 \x01(\t\"d\n\x0eListProjectDto\x12\x11\n\x04page\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x11\n\x04size\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x07\n\x05_pageB\x07\n\x05_sizeB\x07\n\x05_name\"\xd2\x01\n\x0cProjectModel\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ncreated_at\x18\x02 \x01(\t\x12\x12\n\nupdated_at\x18\x03 \x01(\t\x12\x13\n\x0b\x63reate_user\x18\x04 \x01(\x05\x12\x13\n\x0bupdate_user\x18\x05 \x01(\x05\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\r\n\x05owner\x18\x07 \x01(\x05\x12\x0f\n\x07private\x18\x08 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\t \x01(\t\x12\x14\n\x0c\x64ingtalk_url\x18\n \x01(\t\x12\x0b\n\x03\x61pp\x18\x0b \x01(\t\"E\n\x17ListProjectResponseData\x12\x1b\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\r.ProjectModel\x12\r\n\x05total\x18\x02 \x01(\x05\"[\n\x16ListProjectResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12&\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x18.ListProjectResponseData\x12\x0b\n\x03msg\x18\x03 \x01(\t\"\xdf\x02\n\nProjectDto\x12\x0f\n\x02id\x18\x07 \x01(\x05H\x00\x88\x01\x01\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03\x61pp\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\x05\x12\x14\n\x07private\x18\x04 \x01(\x08H\x01\x88\x01\x01\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x14\n\x0c\x64ingtalk_url\x18\x06 \x01(\t\x12\x13\n\x06\x61vatar\x18\x0c \x01(\tH\x02\x88\x01\x01\x12\x17\n\ncreated_at\x18\x0b \x01(\tH\x03\x88\x01\x01\x12\x17\n\nupdated_at\x18\x08 \x01(\tH\x04\x88\x01\x01\x12\x18\n\x0b\x63reate_user\x18\t \x01(\x05H\x05\x88\x01\x01\x12\x18\n\x0bupdate_user\x18\n \x01(\x05H\x06\x88\x01\x01\x42\x05\n\x03_idB\n\n\x08_privateB\t\n\x07_avatarB\r\n\x0b_created_atB\r\n\x0b_updated_atB\x0e\n\x0c_create_userB\x0e\n\x0c_update_user\"\x9d\x02\n\x0eProjectRoleDto\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x12\n\nproject_id\x18\x03 \x01(\x05\x12\x19\n\x0cproject_role\x18\x04 \x01(\x05H\x01\x88\x01\x01\x12\x17\n\ncreated_at\x18\x05 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nupdated_at\x18\x06 \x01(\tH\x03\x88\x01\x01\x12\x18\n\x0b\x63reate_user\x18\x07 \x01(\x05H\x04\x88\x01\x01\x12\x18\n\x0bupdate_user\x18\x08 \x01(\x05H\x05\x88\x01\x01\x42\x05\n\x03_idB\x0f\n\r_project_roleB\r\n\x0b_created_atB\r\n\x0b_updated_atB\x0e\n\x0c_create_userB\x0e\n\x0c_update_user\"P\n\x10QueryProjectData\x12\x1c\n\x07project\x18\x01 \x01(\x0b\x32\x0b.ProjectDto\x12\x1e\n\x05roles\x18\x02 \x03(\x0b\x32\x0f.ProjectRoleDto\"U\n\x17QueryProjectResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x1f\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x11.QueryProjectData\x12\x0b\n\x03msg\x18\x03 \x01(\t\"C\n\x18QueryUserProjectResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x05\"I\n\x10ProjectAvatarDto\x12\x12\n\nproject_id\x18\x01 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"C\n\x18ProjectAvatarResponseDto\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\"&\n\x13QueryUserProjectDto\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\"I\n\x1eQueryUserProjectAmountResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x05\x32\x83\x05\n\x07project\x12\x32\n\x04list\x12\x0f.ListProjectDto\x1a\x17.ListProjectResponseDto\"\x00\x12)\n\x06insert\x12\x0b.ProjectDto\x1a\x10.ProjectResponse\"\x00\x12>\n\x0cupdateAvatar\x12\x11.ProjectAvatarDto\x1a\x19.ProjectAvatarResponseDto\"\x00\x12)\n\x06update\x12\x0b.ProjectDto\x1a\x10.ProjectResponse\"\x00\x12+\n\x05query\x12\x06.Query\x1a\x18.QueryProjectResponseDto\"\x00\x12$\n\x06\x64\x65lete\x12\x06.Query\x1a\x10.ProjectResponse\"\x00\x12\x31\n\ninsertRole\x12\x0f.ProjectRoleDto\x1a\x10.ProjectResponse\"\x00\x12\x31\n\nupdateRole\x12\x0f.ProjectRoleDto\x1a\x10.ProjectResponse\"\x00\x12(\n\ndeleteRole\x12\x06.Query\x1a\x10.ProjectResponse\"\x00\x12;\n\x0f\x63heckPermission\x12\x0e.PermissionDto\x1a\x16.PermissionResponseDto\"\x00\x12L\n\x16queryUserProjectAmount\x12\x0f.ProjectRequest\x1a\x1f.QueryUserProjectAmountResponse\"\x00\x12@\n\x10queryUserProject\x12\x0f.ProjectRequest\x1a\x19.QueryUserProjectResponse\"\x00\x62\x06proto3')



_PROJECTREQUEST = DESCRIPTOR.message_types_by_name['ProjectRequest']
_QUERY = DESCRIPTOR.message_types_by_name['Query']
_PROJECTRESPONSE = DESCRIPTOR.message_types_by_name['ProjectResponse']
_PERMISSIONDTO = DESCRIPTOR.message_types_by_name['PermissionDto']
_PERMISSIONRESPONSEDTO = DESCRIPTOR.message_types_by_name['PermissionResponseDto']
_LISTPROJECTDTO = DESCRIPTOR.message_types_by_name['ListProjectDto']
_PROJECTMODEL = DESCRIPTOR.message_types_by_name['ProjectModel']
_LISTPROJECTRESPONSEDATA = DESCRIPTOR.message_types_by_name['ListProjectResponseData']
_LISTPROJECTRESPONSEDTO = DESCRIPTOR.message_types_by_name['ListProjectResponseDto']
_PROJECTDTO = DESCRIPTOR.message_types_by_name['ProjectDto']
_PROJECTROLEDTO = DESCRIPTOR.message_types_by_name['ProjectRoleDto']
_QUERYPROJECTDATA = DESCRIPTOR.message_types_by_name['QueryProjectData']
_QUERYPROJECTRESPONSEDTO = DESCRIPTOR.message_types_by_name['QueryProjectResponseDto']
_QUERYUSERPROJECTRESPONSE = DESCRIPTOR.message_types_by_name['QueryUserProjectResponse']
_PROJECTAVATARDTO = DESCRIPTOR.message_types_by_name['ProjectAvatarDto']
_PROJECTAVATARRESPONSEDTO = DESCRIPTOR.message_types_by_name['ProjectAvatarResponseDto']
_QUERYUSERPROJECTDTO = DESCRIPTOR.message_types_by_name['QueryUserProjectDto']
_QUERYUSERPROJECTAMOUNTRESPONSE = DESCRIPTOR.message_types_by_name['QueryUserProjectAmountResponse']
ProjectRequest = _reflection.GeneratedProtocolMessageType('ProjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectRequest)
  })
_sym_db.RegisterMessage(ProjectRequest)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), {
  'DESCRIPTOR' : _QUERY,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:Query)
  })
_sym_db.RegisterMessage(Query)

ProjectResponse = _reflection.GeneratedProtocolMessageType('ProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectResponse)
  })
_sym_db.RegisterMessage(ProjectResponse)

PermissionDto = _reflection.GeneratedProtocolMessageType('PermissionDto', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:PermissionDto)
  })
_sym_db.RegisterMessage(PermissionDto)

PermissionResponseDto = _reflection.GeneratedProtocolMessageType('PermissionResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONRESPONSEDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:PermissionResponseDto)
  })
_sym_db.RegisterMessage(PermissionResponseDto)

ListProjectDto = _reflection.GeneratedProtocolMessageType('ListProjectDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ListProjectDto)
  })
_sym_db.RegisterMessage(ListProjectDto)

ProjectModel = _reflection.GeneratedProtocolMessageType('ProjectModel', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTMODEL,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectModel)
  })
_sym_db.RegisterMessage(ProjectModel)

ListProjectResponseData = _reflection.GeneratedProtocolMessageType('ListProjectResponseData', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTRESPONSEDATA,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ListProjectResponseData)
  })
_sym_db.RegisterMessage(ListProjectResponseData)

ListProjectResponseDto = _reflection.GeneratedProtocolMessageType('ListProjectResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _LISTPROJECTRESPONSEDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ListProjectResponseDto)
  })
_sym_db.RegisterMessage(ListProjectResponseDto)

ProjectDto = _reflection.GeneratedProtocolMessageType('ProjectDto', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectDto)
  })
_sym_db.RegisterMessage(ProjectDto)

ProjectRoleDto = _reflection.GeneratedProtocolMessageType('ProjectRoleDto', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTROLEDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectRoleDto)
  })
_sym_db.RegisterMessage(ProjectRoleDto)

QueryProjectData = _reflection.GeneratedProtocolMessageType('QueryProjectData', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPROJECTDATA,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:QueryProjectData)
  })
_sym_db.RegisterMessage(QueryProjectData)

QueryProjectResponseDto = _reflection.GeneratedProtocolMessageType('QueryProjectResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _QUERYPROJECTRESPONSEDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:QueryProjectResponseDto)
  })
_sym_db.RegisterMessage(QueryProjectResponseDto)

QueryUserProjectResponse = _reflection.GeneratedProtocolMessageType('QueryUserProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUSERPROJECTRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:QueryUserProjectResponse)
  })
_sym_db.RegisterMessage(QueryUserProjectResponse)

ProjectAvatarDto = _reflection.GeneratedProtocolMessageType('ProjectAvatarDto', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTAVATARDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectAvatarDto)
  })
_sym_db.RegisterMessage(ProjectAvatarDto)

ProjectAvatarResponseDto = _reflection.GeneratedProtocolMessageType('ProjectAvatarResponseDto', (_message.Message,), {
  'DESCRIPTOR' : _PROJECTAVATARRESPONSEDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:ProjectAvatarResponseDto)
  })
_sym_db.RegisterMessage(ProjectAvatarResponseDto)

QueryUserProjectDto = _reflection.GeneratedProtocolMessageType('QueryUserProjectDto', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUSERPROJECTDTO,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:QueryUserProjectDto)
  })
_sym_db.RegisterMessage(QueryUserProjectDto)

QueryUserProjectAmountResponse = _reflection.GeneratedProtocolMessageType('QueryUserProjectAmountResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUSERPROJECTAMOUNTRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:QueryUserProjectAmountResponse)
  })
_sym_db.RegisterMessage(QueryUserProjectAmountResponse)

_PROJECT = DESCRIPTOR.services_by_name['project']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PROJECTREQUEST._serialized_start=17
  _PROJECTREQUEST._serialized_end=54
  _QUERY._serialized_start=56
  _QUERY._serialized_end=75
  _PROJECTRESPONSE._serialized_start=77
  _PROJECTRESPONSE._serialized_end=135
  _PERMISSIONDTO._serialized_start=137
  _PERMISSIONDTO._serialized_end=227
  _PERMISSIONRESPONSEDTO._serialized_start=229
  _PERMISSIONRESPONSEDTO._serialized_end=293
  _LISTPROJECTDTO._serialized_start=295
  _LISTPROJECTDTO._serialized_end=395
  _PROJECTMODEL._serialized_start=398
  _PROJECTMODEL._serialized_end=608
  _LISTPROJECTRESPONSEDATA._serialized_start=610
  _LISTPROJECTRESPONSEDATA._serialized_end=679
  _LISTPROJECTRESPONSEDTO._serialized_start=681
  _LISTPROJECTRESPONSEDTO._serialized_end=772
  _PROJECTDTO._serialized_start=775
  _PROJECTDTO._serialized_end=1126
  _PROJECTROLEDTO._serialized_start=1129
  _PROJECTROLEDTO._serialized_end=1414
  _QUERYPROJECTDATA._serialized_start=1416
  _QUERYPROJECTDATA._serialized_end=1496
  _QUERYPROJECTRESPONSEDTO._serialized_start=1498
  _QUERYPROJECTRESPONSEDTO._serialized_end=1583
  _QUERYUSERPROJECTRESPONSE._serialized_start=1585
  _QUERYUSERPROJECTRESPONSE._serialized_end=1652
  _PROJECTAVATARDTO._serialized_start=1654
  _PROJECTAVATARDTO._serialized_end=1727
  _PROJECTAVATARRESPONSEDTO._serialized_start=1729
  _PROJECTAVATARRESPONSEDTO._serialized_end=1796
  _QUERYUSERPROJECTDTO._serialized_start=1798
  _QUERYUSERPROJECTDTO._serialized_end=1836
  _QUERYUSERPROJECTAMOUNTRESPONSE._serialized_start=1838
  _QUERYUSERPROJECTAMOUNTRESPONSE._serialized_end=1911
  _PROJECT._serialized_start=1914
  _PROJECT._serialized_end=2557
# @@protoc_insertion_point(module_scope)
