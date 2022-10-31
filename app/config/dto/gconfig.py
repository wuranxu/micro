from pydantic import BaseModel


class GConfigDto(BaseModel):
    id: int = None
    key: str
    value: str
    env: str = None
    key_type: int
    enable: bool


class QueryGConfigDto(BaseModel):
    page: int = 1
    size: int = 8
    env: int = None
    key: str = ""
