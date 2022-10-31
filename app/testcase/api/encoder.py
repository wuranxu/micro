from klose.request.fatcory import PityResponse

from proto.testcase_pb2 import ListTestCaseDataModel


def render_repeated(data, dto, include=(), exclude=()):
    ans = dict()
    for k, v in data.items():
        temp = []
        for item in v:
            temp.append(PityResponse.from_orm(item, dto(), include, exclude))
        ans[k] = ListTestCaseDataModel(test_data=temp)
    return ans
