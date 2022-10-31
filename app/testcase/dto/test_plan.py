from typing import List

from klose.request import PityModel
from pydantic import BaseModel, validator


class PityTestPlanForm(BaseModel):
    id: int = None
    project_id: int
    name: str
    priority: str
    env: List[int]
    cron: str
    ordered: bool
    case_list: List[int]
    pass_rate: int
    receiver: List[int] = list()
    msg_type: List[int] = list()
    retry_minutes: int = 0

    @validator("case_list", "project_id", "env", "cron", "ordered", "priority", "name", "pass_rate")
    def name_not_empty(cls, v):
        return PityModel.not_empty(v)
