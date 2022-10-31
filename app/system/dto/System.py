from pydantic import BaseModel, EmailStr


class EmailDto(BaseModel):
    sender: EmailStr
    password: str
    host: str
    to: str


class YapiDto(BaseModel):
    token: str


class OssDto(BaseModel):
    oss_type: str
    access_key_id: str
    access_key_secret: str
    bucket: str
    endpoint: str = ""


class SystemConfigDto(BaseModel):
    email: EmailDto
    yapi: YapiDto
    oss: OssDto


class EmailDataDto(BaseModel):
    subject: str
    content: str
    attachment: str = None
    receiver: list
