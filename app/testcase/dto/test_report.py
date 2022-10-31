from typing import TypeVar

from pydantic import BaseModel

Author = TypeVar("Author", int, str)


class ListTestReportDto(BaseModel):
    page: int = 1
    size: int = 8
    start_time: str
    end_time: str
    executor: int = None
