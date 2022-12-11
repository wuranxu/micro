import asyncio
import json

from klose.config import Config
from klose.core.msg.mail import Email
from klose.request.fatcory import PityResponse
from klose.third_party.auth import UserToken
from klose.utils.AsyncHttpClient import AsyncRequest
from klose.utils.context import Context, Interceptor
from klose.utils.des import Des

from curd.UserDao import PityUserDao
from dto.User import UserLoginRequest, UserRegisterRequest, UserUpdateForm, ResetPwdForm, \
    GenerateUrlRequest, GithubLoginCode, CustomDto, CheckTokenDto, UserTouchDto
from proto.user_pb2 import LoginResponseDto, UserInfo, ListUserResponseDto, CheckResetUrlResponseDto, \
    UserResponse as Response, ListUserTouchResponse, UserTouchResponse
from proto.user_pb2_grpc import userServicer

FORBIDDEN = "对不起，你没有足够的权限"


class UserServiceApi(userServicer):
    @Interceptor(UserLoginRequest, LoginResponseDto, role=None)
    async def login(self, request, context):
        """
        用户登录
        """
        user = await PityUserDao.login(request.username, request.password)
        data = UserInfo(email=user.email, role=user.role, name=user.name, id=user.id,
                        last_login_at=user.last_login_at.strftime("%Y-%m-%d %H:%M:%S"), avatar=user.avatar)
        user = PityResponse.model_to_dict(user, "password")
        data.expire, data.token = UserToken.get_token(user)
        return data

    @Interceptor(None, ListUserResponseDto)
    async def listUser(self, request, context):
        """
        获取用户列表
        :param request:
        :param context:
        :return:
        """
        users = await PityUserDao.list_users()
        return PityResponse.from_orm_list(users, UserInfo, exclude=("password",))

    @Interceptor(UserRegisterRequest, Response, role=None)
    async def register(self, request, context):
        """
        注册用户
        :param request:
        :param context:
        :return:
        """
        return await PityUserDao.register_user(**request.dict())

    @Interceptor(UserUpdateForm, LoginResponseDto)
    async def update(self, request, context):
        """
        更新用户信息
        :param request:
        :param context:
        :return:
        """
        user_info = Context.get_user(context)
        if user_info.role != Config.ADMIN:
            if user_info.id != request.id:
                # 既不是改自己的资料，也不是超管
                raise PermissionError
            # 如果不是超管，说明是自己改自己，不允许自己改自己的角色
            user_info.role = None
        user = await PityUserDao.update_user(request, user_info.id)
        return UserInfo(id=user.id, email=user.email, role=user.role, name=user.name)

    @Interceptor(CustomDto, LoginResponseDto)
    async def delete(self, request, context):
        """
        删除用户
        :param request:
        :param context:
        :return:
        """
        user_info = Context.get_user(context)
        return await PityUserDao.delete_user(request.id, user_info.id)

    @Interceptor(ResetPwdForm, Response, role=None)
    async def resetPassword(self, request, context):
        """
        重置用户密码
        :param request:
        :param context:
        :return:
        """
        email = Des.des_decrypt(request.token)
        await PityUserDao.reset_password(email, request.password)

    @Interceptor(CheckTokenDto, CheckResetUrlResponseDto, role=None)
    async def checkToken(self, request, context):
        email = Des.des_decrypt(request.token)
        return email

    @Interceptor(GenerateUrlRequest, Response, role=None)
    async def generatePassword(self, request, context):
        """
        生成密码
        :param request:
        :param context:
        :return:
        """
        user = await PityUserDao.query_user_by_email(request.email)
        if user is not None:
            # 说明邮件存在，发送邮件
            em = Des.des_encrypt(request.email)
            link = f"""https://pity.fun/#/user/resetPassword?token={em}"""
            render_html = Email.render_html(Config.PASSWORD_HTML_PATH, link=link, name=user.name)
            asyncio.create_task(Email.send_msg("重置你的pity密码", render_html, None, request.email))

    @Interceptor(GithubLoginCode, LoginResponseDto, role=None)
    async def loginWithGithub(self, request, context):
        """
        通过github登录pity
        :param request:
        :param context:
        :return:
        """
        request.code = request.code.strip("#/")
        client = AsyncRequest(Config.GITHUB_ACCESS, params=dict(client_id=Config.CLIENT_ID,
                                                                client_secret=Config.SECRET_KEY,
                                                                code=request.code))
        res = await client.invoke("GET")
        token = res.get("response").split("&")[0].split("=")[1]
        client.url = Config.GITHUB_USER
        client.kwargs = dict(headers={"Authorization": "token {}".format(token)})
        user_info = await client.invoke("GET")
        user_info = json.loads(user_info.get('response'))
        user = await PityUserDao.register_for_github(user_info.get("login"), user_info.get("name"),
                                                     user_info.get("email"),
                                                     user_info.get("avatar_url"))
        data = UserInfo(email=user.email, role=user.role, name=user.name, id=user.id,
                        last_login_at=user.last_login_at.strftime("%Y-%m-%d %H:%M:%S"), avatar=user.avatar)
        user = PityResponse.model_to_dict(user, "password")
        data.expire, data.token = UserToken.get_token(user)
        return data

    @Interceptor(CustomDto, LoginResponseDto)
    async def query(self, request: CustomDto, context):
        user = await PityUserDao.query_user(request.id)
        return PityResponse.from_orm(user, UserInfo())

    @Interceptor(UserTouchDto, ListUserTouchResponse)
    async def listUserTouch(self, request: UserTouchDto, context):
        data = await PityUserDao.list_user_touch(*request.receivers)
        return Context.render_list(data, UserTouchResponse)
