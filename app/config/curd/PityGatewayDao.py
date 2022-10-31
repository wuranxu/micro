from klose.model import async_session
from klose.third_party.sql import Mapper, ModelWrapper

from model.address import PityGateway
from sqlalchemy import select


@ModelWrapper(PityGateway)
class PityGatewayDao(Mapper):

    @staticmethod
    # @RedisHelper.cache(f"gateway", 1800)
    async def query_gateway(env, name):
        async with async_session() as session:
            query = await session.execute(select(PityGateway).where(PityGateway.deleted_at == 0, PityGateway.env == env,
                                                                    PityGateway.name == name))
            data = query.scalars().first()
            if data is None:
                raise Exception(f"此环境没有网关配置: {name}")
            return data.gateway
