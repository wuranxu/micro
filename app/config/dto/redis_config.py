from pydantic import BaseModel


class RedisConfigDto(BaseModel):
    id: int = None
    name: str
    addr: str
    db: int = 0
    password: str = ''
    cluster: bool = False
    env: int


class QueryRedisDto(BaseModel):
    name: str = ""
    addr: str = ""
    env: int = None
    cluster: bool = None


class RedisCommandDto(BaseModel):
    id: int
    command: str
