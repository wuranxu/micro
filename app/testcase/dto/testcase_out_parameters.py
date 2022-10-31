from typing import List

from klose.request import PityModel
from pydantic import BaseModel, validator


class PityTestCaseOutParametersForm(BaseModel):
    id: int = None
    # case_id: int = None
    name: str
    expression: str = None
    match_index: str = None
    source: int

    @validator("name", "source")
    def name_not_empty(cls, v):
        return PityModel.not_empty(v)


class BatchTestCaseOutParametersDto(BaseModel):
    data: List[PityTestCaseOutParametersForm]
    case_id: int
