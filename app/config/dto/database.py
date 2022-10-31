from pydantic import BaseModel


class DatabaseDto(BaseModel):
    id: int = None
    name: str
    host: str
    port: int = None
    username: str
    password: str
    database: str
    sql_type: int
    env: int


class QueryDatabaseDto(BaseModel):
    name: str = ""
    database: str = ""
    env: int = None


class TestDatabaseDto(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str
    sql_type: int


class RunSQLCommandDto(BaseModel):
    id: int
    sql: str


class QuerySQLHistoryDto(BaseModel):
    page: int = 1
    size: int = 4
