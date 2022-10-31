from klose.model import async_session
from klose.third_party.sql import ModelWrapper, Mapper
from sqlalchemy import select

from dto.environment import EnvironmentDto
from model.environment import Environment


@ModelWrapper(Environment)
class EnvironmentDao(Mapper):

    @staticmethod
    async def query_env(id: int):
        """
        环境id
        :param id:
        :return:
        """
        async with async_session() as session:
            ans = await session.execute(select(Environment).where(Environment.id == id, Environment.deleted_at == 0))
            if ans is None:
                raise Exception(f"环境: {id}不存在")
            return ans.scalars().first()

    @classmethod
    async def insert_env(cls, data: EnvironmentDto, user):
        try:
            async with async_session() as session:
                async with session.begin():
                    query = await session.execute(
                        select(Environment).where(Environment.name == data.name, Environment.deleted_at == 0))
                    if query.scalars().first() is not None:
                        raise Exception(f"环境已存在")
                    env = Environment(**data.dict(), user=user)
                    session.add(env)
        except Exception as e:
            EnvironmentDao.__log__.error(f"新增环境: {data.name}失败, {e}")
            raise Exception(f"添加失败: {str(e)}")

    @classmethod
    async def list_env(cls, name: str = ""):
        try:
            search = [Environment.deleted_at == 0]
            async with async_session() as session:
                if name:
                    search.append(Environment.name.like("%{}%".format(name)))
                sql = select(Environment).where(*search)
                query = await session.execute(sql)
                return query.scalars().all()
        except Exception as e:
            cls.__log__.error(f"获取环境列表失败, {str(e)}")
            raise Exception(f"获取环境数据失败: {str(e)}")
