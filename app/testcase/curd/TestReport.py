from datetime import datetime

from klose.model import async_session
from klose.third_party.sql import ModelWrapper, Mapper
from sqlalchemy import select, desc

from curd.TestResult import TestResultDao
from model.report import PityReport
from model.test_plan import PityTestPlan


@ModelWrapper(PityReport)
class TestReportDao(Mapper):

    @staticmethod
    async def start(executor: int, env: int, mode: int = 0, plan_id: int = None) -> int:
        """
        生成buildId，开始执行任务，任务完成后通过回调方法更新报告
        :return: 返回report_id
        """
        try:
            async with async_session() as session:
                async with session.begin():
                    report = PityReport(executor, env, mode=mode, plan_id=plan_id)
                    session.add(report)
                    await session.flush()
                    return report.id
        except Exception as e:
            TestReportDao.log.error(f"新增报告失败, error: {e}")
            raise Exception("新增报告失败")

    @staticmethod
    async def update(report_id: int, status) -> None:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(PityReport).where(PityReport.id == report_id)
                    data = await session.execute(sql)
                    report = data.scalars().first()
                    if report is None:
                        raise Exception("更新报告失败")
                    report.status = status
                    await session.flush()
        except Exception as e:
            TestReportDao.log.error(f"更新报告失败, error: {e}")
            raise Exception("更新报告失败")

    @staticmethod
    async def end(report_id: int, success_count: int, failed_count: int,
                  error_count: int, skipped_count: int, status: int, cost: str) -> PityReport:
        try:
            async with async_session() as session:
                async with session.begin():
                    sql = select(PityReport).where(PityReport.id == report_id)
                    data = await session.execute(sql)
                    report = data.scalars().first()
                    if report is None:
                        raise Exception("更新报告失败")
                    report.status = status
                    report.success_count = success_count
                    report.failed_count = failed_count
                    report.error_count = error_count
                    report.skipped_count = skipped_count
                    report.cost = cost
                    report.finished_at = datetime.now()
                    await session.flush()
                    session.expunge(report)
                    return report
        except Exception as e:
            TestReportDao.log.error(f"更新报告失败, error: {e}")
            raise Exception("更新报告失败")

    @staticmethod
    async def query(report_id: int):
        """
        根据报告id查询报告
        :param report_id:
        :return:
        """
        try:
            async with async_session() as session:
                sql = select(PityReport, PityTestPlan.name).outerjoin(PityTestPlan,
                                                                      PityTestPlan.id == PityReport.plan_id
                                                                      ).where(PityReport.id == report_id)
                data = await session.execute(sql)
                if data is None:
                    raise Exception("报告不存在")
                report, plan_name = data.first()
                test_data = await TestResultDao.list(report_id)
                return report, test_data, plan_name
        except Exception as e:
            TestReportDao.__log__.error(f"查询报告失败: {e}")
            raise Exception(f"查询报告失败: {e}")

    @staticmethod
    async def list_report(page: int, size: int, start_time: datetime, end_time: datetime, executor: int or str = None):
        """
        获取报告列表
        :param size:
        :param page:
        :param end_time:
        :param start_time:
        :param executor: int or str
        :return:
        """
        try:
            async with async_session() as session:
                sql = select(PityReport).where(PityReport.start_at.between(start_time, end_time)).order_by(
                    desc(PityReport.start_at))
                if executor is not None:
                    sql = sql.where(PityReport.executor == executor)
                data = await session.execute(sql)
                total = data.raw.rowcount
                if total == 0:
                    return [], 0
                sql = sql.offset((page - 1) * size).limit(size)
                data = await session.execute(sql)
                return data.scalars().all(), total
        except Exception as e:
            TestReportDao.log.error(f"查询构建记录失败: {e}")
            raise Exception(f"查询构建记录失败: {e}")
