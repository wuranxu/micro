from core.paramters.jsonpath_parser import JSONPathParser
from core.paramters.kv_parser import HeaderParser, CookieParser
from core.paramters.regex_parser import RegexParser
from core.paramters.status_code_parser import StatusCodeParser
from enums.CaseParametersEnum import CaseParametersEnum


def ParametersParser(parameter_type: CaseParametersEnum):
    if parameter_type == CaseParametersEnum.TEXT:
        return RegexParser.parse
    if parameter_type == CaseParametersEnum.JSON:
        return JSONPathParser.parse
    if parameter_type == CaseParametersEnum.HEADER:
        return HeaderParser.parse
    if parameter_type == CaseParametersEnum.COOKIE:
        return CookieParser.parse
    return StatusCodeParser.parse
