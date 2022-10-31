from typing import List

from pydantic import BaseModel

from dto.constructor import ConstructorForm
from dto.request import RequestInfo
from dto.testcase_data import PityTestcaseDataForm
from dto.testcase_out_parameters import PityTestCaseOutParametersForm
from enums.ConvertorEnum import CaseConvertorType


class ListTestCaseForm(BaseModel):
    directory_id: int = None
    name: str = ""
    create_user: str = ""


class DeleteTestCaseDto(BaseModel):
    data: List[int]


class TestCaseForm(BaseModel):
    id: int = None
    priority: str
    url: str = ""
    name: str = ""
    case_type: int = 0
    base_path: str = None
    tag: str = None
    body: str = None
    body_type: int = 0
    request_headers: str = None
    request_method: str = None
    status: int
    out_parameters: List[PityTestCaseOutParametersForm] = []
    directory_id: int
    request_type: int


class TestCaseAssertsForm(BaseModel):
    id: int = None
    name: str
    case_id: int = None
    assert_type: str
    expected: str
    actually: str


class TestCaseInfo(BaseModel):
    case: TestCaseForm
    asserts: List[TestCaseAssertsForm] = []
    data: List[PityTestcaseDataForm] = []
    constructor: List[ConstructorForm] = []
    out_parameters: List[PityTestCaseOutParametersForm] = []


class TestCaseGeneratorForm(BaseModel):
    directory_id: int
    requests: List[RequestInfo]
    name: str


class QueryTestCaseForm(BaseModel):
    caseId: int


class CommonIdForm(BaseModel):
    id: int


class QueryTestPlanCaseDto(BaseModel):
    project_id: int


class QueryTestCaseDirDto(BaseModel):
    project_id: int
    move: bool = False


class QueryTestCaseDto(BaseModel):
    directory_id: int


class ImportTestCaseDto(BaseModel):
    convertor: CaseConvertorType
    filename: str
    content: bytes
