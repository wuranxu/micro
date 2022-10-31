from typing import List

from pydantic import BaseModel

from dto.constructor import ConstructorIndex


class ListTestCaseDto(BaseModel):
    directory_id: int = None
    name: str = ""
    create_user: int = None


class QueryTestCaseDto(BaseModel):
    case_id: int


class DeleteTestCaseDto(BaseModel):
    id_list: List[int]


class ReOrderConstructorDto(BaseModel):
    data: List[ConstructorIndex]


class ListConstructorQueryForm(BaseModel):
    suffix: bool
    constructor_type: int
