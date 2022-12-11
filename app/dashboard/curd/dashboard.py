from datetime import datetime, timedelta
from typing import List, Dict

from klose.model import async_session
from klose.third_party.Redis import RedisHelper
from klose.third_party.sql import Mapper, connect
from sqlalchemy import select, func, and_, desc, asc
from sqlalchemy.ext.asyncio import AsyncSession

from model.project import Project
from model.report import PityReport
from model.test_case import TestCase
from model.test_plan import PityTestPlan
from model.user import PityUser


class Item(object):
    def __init__(self, name, model):
        self.name = name
        self.model = model


class DashboardDao(Mapper):

    @classmethod
    @connect
    async def get_statistics_data(cls, start: datetime, end: datetime, session: AsyncSession = None):
        return await cls.get_model_statistic_data(start, end, session, Item("project", Project),
                                                  Item("testcase", TestCase),
                                                  Item("testplan", PityTestPlan),
                                                  Item("user", PityUser))

    @classmethod
    @RedisHelper.cache("report_statistics")
    @connect
    async def get_report_statistics(cls, start: datetime, end: datetime, session: AsyncSession = None):
        result, idx = await cls.get_date_data(start, end)
        sql = cls.create_sql(PityReport, start, end, field="start_at")
        data = await session.execute(sql)
        count = success = failed = skip = error = total = total_pass = 0
        for item in data.scalars().all():
            date = item.start_at.strftime("%Y-%m-%d")
            count += 1
            total_pass += item.success_count
            total += item.success_count + item.failed_count + item.error_count
            success += item.success_count
            failed += item.failed_count
            error += item.error_count
            skip += item.skipped_count
            result[idx[date]]["count"] = result[idx[date]].get("count", 0) + 1
            result[idx[date]]["success"] = result[idx[date]].get("success", 0) + item.success_count
            result[idx[date]]["failed"] = result[idx[date]].get("failed", 0) + item.failed_count
            result[idx[date]]["error"] = result[idx[date]].get("error", 0) + item.error_count
            result[idx[date]]["skip"] = result[idx[date]].get("skip", 0) + item.skipped_count
            date_total = result[idx[date]]["success"] + result[idx[date]]["failed"] + result[idx[date]]["error"]
            if total == 0:
                result[idx[date]]["rate"] = 0.00
            else:
                result[idx[date]]["rate"] = round(result[idx[date]]["success"] / date_total * 100, 2)
        rate = round(total_pass / total * 100, 2) if total > 0 else 0.00
        return dict(count=count, success=success, failed=failed, skip=skip, error=error, data=result, rate=rate)

    @classmethod
    async def get_model_statistic_data(cls, start: datetime, end: datetime, session: AsyncSession = None, *names: Item):
        result, idx = await cls.get_date_data(start, end)
        data = dict()
        for n in names:
            query = await session.execute(cls.create_sql(n.model, start, end))
            # 找到未删除的所有项目数据
            counts = await session.execute(select(func.count(n.model.id)).where(n.model.deleted_at == 0))
            for r in query.scalars().all():
                date = r.created_at.strftime("%Y-%m-%d")
                if result[idx[date]].get(n.name) is None:
                    result[idx[date]][n.name] = 1
                else:
                    result[idx[date]][n.name] += 1
            data[n.name] = counts.first().count
        return data, result

    @classmethod
    def create_sql(cls, model, start: datetime, end: datetime, *condition, field='created_at'):
        start_str = start.replace(hour=0, minute=0, second=0, microsecond=0)
        end_str = end.replace(hour=23, minute=59, second=59)
        return select(model).where(getattr(model, field) >= start_str, getattr(model, field) <= end_str,
                                   *condition)

    @classmethod
    async def get_date_data(cls, start: datetime, end: datetime):
        ans = []
        date_index = dict()
        start_time = start.replace(hour=0, minute=0, second=0, microsecond=0)
        while start_time <= end:
            date = start_time.strftime("%Y-%m-%d")
            ans.append({"date": date})
            date_index[date] = len(ans) - 1
            start_time += timedelta(days=1)
        return ans, date_index

    @classmethod
    async def generate_sql(cls):
        return select(TestCase.create_user, func.count(TestCase.id)) \
            .outerjoin(PityUser, and_(PityUser.deleted_at == 0, TestCase.create_user == PityUser.id)).where(
            TestCase.deleted_at == 0).group_by(TestCase.create_user).order_by(
            desc(func.count(TestCase.id)))

    @classmethod
    @RedisHelper.cache("rank")
    @connect
    async def query_user_case_list(cls, session: AsyncSession = None) -> Dict[str, List]:
        """
        created by woody at 2022-02-13 12:59
        查询用户case数量和排名
        :return:
        """
        ans = dict()
        sql = await cls.generate_sql()
        query = await session.execute(sql)
        for i, q in enumerate(query.all()):
            user, count = q
            ans[str(user)] = [count, i + 1]
        return ans

    @classmethod
    @RedisHelper.cache("rank_detail")
    @connect
    async def query_user_case_rank(cls, session: AsyncSession = None) -> List:
        ans = []
        sql = await cls.generate_sql()
        query = await session.execute(sql)
        for i, q in enumerate(query.all()):
            user, count = q
            ans.append(dict(id=user, count=count, rank=i + 1))
        return ans

    @staticmethod
    async def fill_data(start_time: datetime, end_time: datetime, data: dict):
        """
        填补数据
        :param data:
        :param start_time:
        :param end_time:
        :return:
        """
        start = start_time
        ans = []
        while start <= end_time:
            date = start.strftime("%Y-%m-%d")
            ans.append(dict(date=date, count=data.get(date, 0)))
            start += timedelta(days=1)
        return ans

    @staticmethod
    async def query_weekly_user_case(user_id: int, start_time: datetime, end_time: datetime) -> List:
        ans = dict()
        async with async_session() as session:
            async with session.begin():
                # date_ = func.date_format(TestCase.created_at, "%Y-%m-%d")
                sql = select(TestCase.created_at, func.count(TestCase.id)).where(
                    TestCase.create_user == user_id,
                    TestCase.deleted_at == 0, TestCase.created_at.between(start_time, end_time)).group_by(
                    TestCase.created_at).order_by(asc(TestCase.created_at))
                query = await session.execute(sql)
                for i, q in enumerate(query.all()):
                    date, count = q
                    ans[date.strftime("%Y-%m-%d")] = count
        return await DashboardDao.fill_data(start_time, end_time, ans)
