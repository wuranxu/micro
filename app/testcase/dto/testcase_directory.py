from typing import List

from klose.request import PityModel
from pydantic import BaseModel, validator


class PityTestCaseDirectoryDto(BaseModel):
    directory_id: int


class PityTestcaseDirectoryForm(BaseModel):
    id: int = None
    name: str
    project_id: int
    parent: int = None

    @validator("name", "project_id")
    def name_not_empty(cls, v):
        return PityModel.not_empty(v)


class PityMoveTestCaseDto(BaseModel):
    project_id: int
    id_list: List[int]
    directory_id: int

    @validator("id_list", "project_id", "directory_id")
    def name_not_empty(cls, v):
        return PityModel.not_empty(v)
