import json

from klose.utils.client import RpcClient

from core.constructor.constructor import ConstructorAbstract
from model.constructor import Constructor


class RedisConstructor(ConstructorAbstract):

    @staticmethod
    async def run(executor, env, index, path, params, req_params, constructor: Constructor, **kwargs):
        try:
            executor.append(f"当前路径: {path}, 第{index + 1}条{ConstructorAbstract.get_name(constructor)}")
            data = json.loads(constructor.constructor_json)
            redis = data.get("redis")
            command = data.get("command")
            executor.append(
                f"当前{ConstructorAbstract.get_name(constructor)}类型为redis, 名称: {redis}\n命令: {command}\n")
            config_service = await RpcClient.get_instance("config")
            result = await config_service.runRedisCommandWithName(dict(env=env, name=redis, command=command))
            if result.get("code", 0) != 0:
                raise Exception(f"执行sql失败, {result.get('msg')}")
            command_result = result.get("data")
            params[constructor.value] = command_result
            executor.append(
                f"当前{ConstructorAbstract.get_name(constructor)}返回变量: {constructor.value}\n返回值:\n {command_result}\n")
        except Exception as e:
            raise Exception(
                f"{path}->{constructor.name} 第{index + 1}个{ConstructorAbstract.get_name(constructor)}执行失败: {e}")
