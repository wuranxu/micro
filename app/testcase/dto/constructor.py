from klose.excpetions.ParamsException import ParamsError
from klose.request import PityModel
from pydantic import BaseModel, validator


class ConstructorForm(BaseModel):
    id: int = None
    value: str = ""
    type: int
    name: str
    index: int = 0
    constructor_json: str
    enable: bool
    case_id: int = None
    public: bool
    suffix: bool

    @validator("name", "constructor_json", "type", "public", "enable", "suffix")
    def name_not_empty(cls, v):
        if isinstance(v, str) and len(v.strip()) == 0:
            raise ParamsError("不能为空")
        if not isinstance(v, int):
            if not v:
                raise ParamsError("不能为空")
        return v


class ConstructorIndex(BaseModel):
    id: int
    index: int

    @validator("id", "index")
    def name_not_empty(cls, v):
        return PityModel.not_empty(v)


class QueryConstructorDto(BaseModel):
    suffix: bool
    name: str = ""


class ListConstructorDto(BaseModel):
    constructor_type: int
    suffix: bool
