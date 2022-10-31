import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import make_msgid

from klose.config import Config
from klose.utils.context import Interceptor

from api.configuration import SystemConfiguration
from dto.System import SystemConfigDto, EmailDataDto
from proto.system_pb2 import SystemResponse, ConfigDto
from proto.system_pb2_grpc import systemServicer


class SystemServiceApi(systemServicer):
    @Interceptor(None, SystemResponse)
    async def getSystemConfig(self, request, context):
        """
        用户登录
        """
        configuration = SystemConfiguration.get_config()
        return ConfigDto(**configuration)

    @Interceptor(SystemConfigDto, SystemResponse, role=Config.ADMIN)
    async def updateSystemConfig(self, request, context):
        """
        更新系统设置
        """
        SystemConfiguration.update_config(request.dict())

    @Interceptor(EmailDataDto, SystemResponse)
    async def sendEmail(self, request, context):
        """
        发送邮件
        """
        configuration = SystemConfiguration.get_config()
        data = configuration.get("email")
        sender = data.get("sender")
        message = MIMEText(request.content, 'html', 'utf-8')
        message['From'] = sender
        # 抄送给自己一份
        message['Subject'] = Header(request.subject, 'utf-8')
        message['Message-ID'] = make_msgid()

        try:
            smtp = smtplib.SMTP()
            smtp.connect(data.get("host"))
            # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
            smtp.set_debuglevel(1)
            smtp.login(sender, data.get("password"))
            smtp.sendmail(sender, [sender, *request.receiver], message.as_string())
        except Exception as e:
            raise Exception(f"发送测试报告邮件失败: {e}")
