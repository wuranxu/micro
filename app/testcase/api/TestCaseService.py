from datetime import datetime

from klose.excpetions.AuthException import AuthException
from klose.model import async_session
from klose.request.fatcory import PityResponse
from klose.utils.client import RpcClient
from klose.utils.context import Context, Interceptor

from api.encoder import render_repeated
from curd.ConstructorDao import ConstructorDao
from curd.TestCaseAssertsDao import TestCaseAssertsDao
from curd.TestCaseDao import TestCaseDao
from curd.TestCaseDirectory import PityTestcaseDirectoryDao
from curd.TestCaseOutParametersDao import PityTestCaseOutParametersDao
from curd.TestReport import TestReportDao
from curd.TestcaseDataDao import PityTestcaseDataDao
from dto.constructor import ConstructorForm, QueryConstructorDto
from dto.test_report import ListTestReportDto
from dto.testcase import ListTestCaseDto, QueryTestCaseDto, ReOrderConstructorDto, ListConstructorQueryForm
from dto.testcase_data import PityTestcaseDataForm
from dto.testcase_directory import PityTestcaseDirectoryForm, PityMoveTestCaseDto, PityTestCaseDirectoryDto
from dto.testcase_out_parameters import PityTestCaseOutParametersForm
from dto.testcase_schema import TestCaseForm, TestCaseInfo, DeleteTestCaseDto, TestCaseAssertsForm, CommonIdForm, \
    QueryTestCaseDirDto, TestCaseGeneratorForm, ImportTestCaseDto, QueryTestPlanCaseDto
from model.out_parameters import PityTestCaseOutParameters
from model.test_case import TestCase
from proto.testcase_pb2 import ListTestCaseResponse, TestCaseModel, TestCaseTree, QueryTestCaseDirTreeResponse, \
    QueryTestCaseDirectoryResponseDto, TestCaseDirectoryModel, QueryTestCaseResponseDto, TestCaseFullResponseData, \
    TestCaseAssertsModel, TestCaseConstructorModel, TestCaseDataModel, TestCaseOutParametersModel, \
    TestCaseResponse, UpdateTestCaseResponseDto, UpdateTestCaseData, TestCaseAssertsResponseDto, \
    QueryConstructorTreeResponse, ConstructorTree, QueryConstructorResponse, ListConstructorResponse, \
    ConstructorResponseTree, QueryReportResponse, QueryReportData, TestReportModel, TestResult, ListReportResponse, \
    ListReportData, QueryXmindResponse, QueryXmindData, TestPlanTreeResponse, TestPlanTreeData, TestCaseDataResponse, \
    TestCaseOutParametersResponse, BatchUpdateOutParametersResponse
from proto.testcase_pb2_grpc import testcaseServicer
from utils.request import get_convertor
from utils.request.generator import CaseGenerator


class TestCaseServiceApi(testcaseServicer):

    @Interceptor(ListTestCaseDto, ListTestCaseResponse)
    async def listTestCase(self, request, context):
        """获取测试用例数据
        :param request:
        :param context:
        :return:
        """
        data = await TestCaseDao.list_test_case(request.directory_id, request.name, request.create_user or None)
        return PityResponse.from_orm_list(data, TestCaseModel)

    # @Interceptor(TestCaseInfo, InsertTestCaseResponseDto)
    # async def insertTestCase(self, request, context):
    #     """添加测试用例
    #     :param request:
    #     :param context:
    #     :return:
    #     """
    #     user = Context.get_user(context)
    #     record = await TestCaseDao.query_record(name=request.name, directory_id=request.directory_id)
    #     if record is not None:
    #         return Context.failed("用例已存在")
    #     model = TestCase(**request.dict(), create_user=user.id)
    #     model = await TestCaseDao.insert(model=model, log=True)
    #     return model.id

    @Interceptor(TestCaseInfo, TestCaseResponse)
    async def createTestCase(self, request, context):
        """创建测试用例，包含前后置条件和断言等数据
        :param request:
        :param context:
        :return:
        """
        user = Context.get_user(context)
        async with async_session() as session:
            async with session.begin():
                await TestCaseDao.insert_test_case(session, request, user.id)

    @Interceptor(TestCaseForm, UpdateTestCaseResponseDto)
    async def updateTestCase(self, request, context):
        """编辑测试用例
        :param request:
        :param context:
        :return:
        """
        user = Context.get_user(context)
        data = await TestCaseDao.update_test_case(request, user.id)
        result = await PityTestCaseOutParametersDao.update_many(request.id, request.out_parameters, user.id)
        return UpdateTestCaseData(
            case_info=PityResponse.from_orm(data, TestCaseModel()),
            out_parameters=PityResponse.from_orm_list(result, TestCaseOutParametersModel)
        )

    @Interceptor(DeleteTestCaseDto, TestCaseResponse)
    async def deleteTestCase(self, request, context):
        """删除测试用例
        :param request:
        :param context:
        :return:
        """
        user = Context.get_user(context)
        async with async_session() as session:
            async with session.begin():
                await TestCaseDao.delete_records(session, user.id, request.data)
                # 删除断言
                await TestCaseAssertsDao.delete_records(session, user.id, request.data, column="case_id")
                # 删除测试数据
                await PityTestcaseDataDao.delete_records(session, user.id, request.data, column="case_id")

    @Interceptor(QueryTestCaseDto, QueryTestCaseResponseDto)
    async def queryTestCase(self, request, context):
        """查询测试用例数据
        :param request:
        :param context:
        :return:
        """
        data = await TestCaseDao.query_test_case(request.case_id)
        resp = TestCaseFullResponseData(
            asserts=PityResponse.from_orm_list(data.get("asserts"), TestCaseAssertsModel),
            constructors=PityResponse.from_orm_list(data.get("constructors"), TestCaseConstructorModel),
            test_data=render_repeated(data.get("test_data"), TestCaseDataModel),
            out_parameters=PityResponse.from_orm_list(data.get("out_parameters"), TestCaseOutParametersModel),
            case=PityResponse.from_orm(data.get("case"), TestCaseModel()),
            constructors_case=PityResponse.from_orm_dict(data.get("constructors_case"), TestCaseModel)
        )
        return resp

    @Interceptor(TestCaseAssertsForm, TestCaseAssertsResponseDto)
    async def insertAsserts(self, request, context):
        """插入断言数据
        :param request:
        :param context:
        :return:
        """
        user = Context.get_user(context)
        new_assert = await TestCaseAssertsDao.insert_test_case_asserts(request, user_id=user.id)
        return PityResponse.from_orm(new_assert, TestCaseAssertsModel())

    @Interceptor(TestCaseAssertsForm, TestCaseAssertsResponseDto)
    async def updateAsserts(self, request, context):
        """修改断言数据
        """
        user = Context.get_user(context)
        updated = await TestCaseAssertsDao.update_test_case_asserts(request, user_id=user.id)
        return PityResponse.from_orm(updated, TestCaseAssertsModel())

    @Interceptor(CommonIdForm, TestCaseResponse)
    async def deleteAsserts(self, request, context):
        """
        删除断言数据
        """
        user = Context.get_user(context)
        await TestCaseAssertsDao.delete_test_case_asserts(request.id, user_id=user.id)

    @Interceptor(ConstructorForm, TestCaseResponse)
    async def insertConstructor(self, request, context):
        """
        插入构造方法
        """
        user = Context.get_user(context)
        await ConstructorDao.insert_constructor(request, user_id=user.id)

    @Interceptor(ConstructorForm, TestCaseResponse)
    async def updateConstructor(self, request, context):
        """
        编辑构造方法
        """
        user = Context.get_user(context)
        await ConstructorDao.update_constructor(request, user_id=user.id)

    @Interceptor(CommonIdForm, TestCaseResponse)
    async def deleteConstructor(self, request, context):
        """
        删除构造方法
        """
        user = Context.get_user(context)
        await ConstructorDao.delete_constructor(request.id, user_id=user.id)

    @Interceptor(ReOrderConstructorDto, TestCaseResponse)
    async def reorderConstructor(self, request, context):
        """
        重新排序构造方法
        """
        await ConstructorDao.update_constructor_index(request.data)

    @Interceptor(QueryConstructorDto, QueryConstructorTreeResponse)
    async def queryConstructorTree(self, request, context):
        result = await ConstructorDao.get_constructor_tree(request.name, request.suffix)
        return Context.render(result, ConstructorTree)

    @Interceptor(CommonIdForm, QueryConstructorResponse)
    async def queryConstructor(self, request, context):
        result = await ConstructorDao.get_constructor_data(request.id)
        return PityResponse.from_orm(result, TestCaseConstructorModel())

    @Interceptor(ListConstructorQueryForm, ListConstructorResponse)
    async def listConstructor(self, request, context):
        ans = await ConstructorDao.get_case_and_constructor(request.constructor_type, request.suffix)
        return Context.render_list(ans, ConstructorResponseTree)

    @Interceptor(CommonIdForm, QueryReportResponse)
    async def queryTestReport(self, request, context):
        """
        查询测试报告
        """
        report, case_list, plan_name = await TestReportDao.query(request.id)
        return QueryReportData(
            report=PityResponse.from_orm(report, TestReportModel()),
            plan_name=plan_name,
            case_list=PityResponse.from_orm_list(case_list, TestResult)
        )

    @Interceptor(ListTestReportDto, ListReportResponse)
    async def listTestReport(self, request, context):
        """
        获取测试报告列表
        """
        start = datetime.strptime(request.start_time, "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime(request.end_time, "%Y-%m-%d %H:%M:%S")
        report_list, total = await TestReportDao.list_report(
            page=request.page, size=request.size, start_time=start, end_time=end, executor=request.executor)
        return ListReportData(data=PityResponse.from_orm_list(report_list, TestReportModel), total=total)

    @Interceptor(CommonIdForm, QueryXmindResponse)
    async def queryXmindData(self, request, context):
        data = await TestCaseDao.get_xmind_data(request.id)
        return Context.render(data, QueryXmindData)

    @Interceptor(QueryTestCaseDirDto, QueryTestCaseDirTreeResponse)
    async def queryTestCaseDirTree(self, request, context):
        """查询用例目录
        """
        tree_data, _ = await PityTestcaseDirectoryDao.get_directory_tree(
            request.project_id, move=request.move)
        return Context.render_list(tree_data, TestCaseTree)

    @Interceptor(QueryTestPlanCaseDto, TestPlanTreeResponse)
    async def queryTestCaseTree(self, request, context):
        """
        获取case目录树
        """
        tree_data, cs_map = await PityTestcaseDirectoryDao.get_directory_tree(request.project_id,
                                                                              TestCaseDao.get_test_case_by_directory_id)
        return TestPlanTreeData(
            tree=Context.render_list(tree_data, TestCaseTree),
            case_map=cs_map
        )

    @Interceptor(PityTestCaseDirectoryDto, QueryTestCaseDirectoryResponseDto)
    async def queryTestCaseDir(self, request, context):
        """
        获取用例目录
        """
        user = Context.get_user(context)
        data = await PityTestcaseDirectoryDao.query_directory(request.directory_id)
        project_service = await RpcClient.get_instance("project")
        result = await project_service.checkPermission(
            dict(user_id=user.id, user_role=user.role, project_id=data.project_id),
            metadata=context.invocation_metadata())
        if result.get("code", 0) != 0:
            raise AuthException
        return PityResponse.from_orm(data, TestCaseDirectoryModel())

    @Interceptor(PityTestcaseDirectoryForm, TestCaseResponse)
    async def insertTestCaseDir(self, request, context):
        """
        添加用例目录
        """
        user = Context.get_user(context)
        await PityTestcaseDirectoryDao.insert_directory(request, user.id)

    @Interceptor(PityTestcaseDirectoryForm, TestCaseResponse)
    async def updateTestCaseDir(self, request, context):
        """
        更新用例目录
        """
        user = Context.get_user(context)
        await PityTestcaseDirectoryDao.update_directory(request, user.id)

    @Interceptor(CommonIdForm, TestCaseResponse)
    async def deleteTestCaseDir(self, request, context):
        """
        删除用例目录
        """
        user = Context.get_user(context)
        await PityTestcaseDirectoryDao.delete_directory(request.id, user.id)

    @Interceptor(PityTestcaseDataForm, TestCaseDataResponse)
    async def insertTestData(self, request, context):
        """
        插入测试数据
        """
        user = Context.get_user(context)
        data = await PityTestcaseDataDao.insert_testcase_data(request, user.id)
        return PityResponse.from_orm(data, TestCaseDataModel())

    @Interceptor(PityTestcaseDataForm, TestCaseDataResponse)
    async def updateTestData(self, request, context):
        """
        更新测试数据
        """
        user = Context.get_user(context)
        data = await PityTestcaseDataDao.update_testcase_data(request, user.id)
        return PityResponse.from_orm(data, TestCaseDataModel())

    @Interceptor(CommonIdForm, TestCaseResponse)
    async def deleteTestData(self, request, context):
        """
        删除测试数据
        """
        user = Context.get_user(context)
        await PityTestcaseDataDao.delete_testcase_data(request.id, user.id)

    @Interceptor(PityMoveTestCaseDto, TestCaseResponse)
    async def moveTestCase(self, request, context):
        """
        移动测试用例
        """
        user = Context.get_user(context)
        project_service = await RpcClient.get_instance("project")
        result = await project_service.checkPermission(
            dict(user_id=user.id, user_role=user.role, project_id=request.project_id),
            metadata=context.invocation_metadata())
        if result.get("code", 0) != 0:
            raise AuthException
        await TestCaseDao.update_by_map(user.id, TestCase.id.in_(request.id_list), directory_id=request.directory_id)

    @Interceptor(PityTestCaseOutParametersForm, TestCaseOutParametersResponse)
    async def insertParams(self, request, context):
        """
        插入提取参数
        """
        user = Context.get_user(context)
        query = await PityTestCaseOutParametersDao.query_record(name=request.name, case_id=request.case_id)
        if query is not None:
            return PityResponse.failed("参数名称已存在")
        data = PityTestCaseOutParameters(**request.dict(), user_id=user.id)
        data = await PityTestCaseOutParametersDao.insert(model=data)
        return PityResponse.from_orm(data, TestCaseOutParametersModel())

    @Interceptor(PityTestCaseOutParametersDao, BatchUpdateOutParametersResponse)
    async def batchUpdateParams(self, request, context):
        """
        批量更新出参提取
        """
        user = Context.get_user(context)
        result = await PityTestCaseOutParametersDao.update_many(request.case_id,
                                                                request.parameters, user.id)
        return PityResponse.from_orm_list(result, TestCaseOutParametersModel)

    @Interceptor(PityTestCaseOutParametersForm, TestCaseOutParametersResponse)
    async def updateParams(self, request, context):
        data = await PityTestCaseOutParametersDao.update_record_by_id(user.id, request)
        return PityResponse.from_orm(data, TestCaseOutParametersModel())

    @Interceptor(CommonIdForm, TestCaseResponse)
    async def deleteParams(self, request, context):
        """
        删除出参
        """
        user = Context.get_user(context)
        async with async_session() as session:
            await PityTestCaseOutParametersDao.delete_record_by_id(session, request.id, user.id, log=False)

    async def generateTestCase(self, request, context):
        """
        生成测试用例
        """
        user = Context.get_user(context)
        dto: TestCaseGeneratorForm = Context.parse_args(request, TestCaseGeneratorForm)
        if len(dto.requests) == 0:
            return Context.failed("无http请求，请检查参数")
        CaseGenerator.extract_field(dto.requests)
        cs = CaseGenerator.generate_case(dto.directory_id, dto.name, dto.requests[-1])
        constructors = CaseGenerator.generate_constructors(dto.requests)
        info = TestCaseInfo(constructor=constructors, case=cs)
        async with async_session() as session:
            async with session.begin():
                ans = await TestCaseDao.insert_test_case(session, info, user.id)
                return Context.success(ans)

    async def importTestCase(self, request, context):
        """
        导入测试用例
        """
        # user = Context.get_user(context)
        dto: ImportTestCaseDto = Context.parse_args(request, ImportTestCaseDto)
        convert, file_ext = get_convertor(dto.convertor)
        if convert is None:
            return Context.failed("不支持的导入数据")
        if not dto.filename.endswith(f".{file_ext}"):
            return Context.failed(f"请传入{file_ext}后缀文件")
        requests = convert(dto.content)
        return Context.success(requests)
