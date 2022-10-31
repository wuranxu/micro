from pydantic import BaseModel


class EnvironmentDto(BaseModel):
    id: int = None
    name: str
    remarks: str = None


class QueryEnvironmentDto(BaseModel):
    name: str = ""
