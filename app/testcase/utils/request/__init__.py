from enums.ConvertorEnum import CaseConvertorType
from utils.request.convertor import Convertor
from utils.request.har_convertor import HarConvertor


def get_convertor(c: CaseConvertorType) -> (Convertor.convert, str):
    if c == CaseConvertorType.har:
        return HarConvertor.convert, CaseConvertorType.har.name
    return None, ""
