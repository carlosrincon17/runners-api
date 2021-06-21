from email.mime.text import MIMEText

from fastapi_mail import ConnectionConfig, MessageSchema, FastMail
from jinja2 import Environment, PackageLoader, select_autoescape

from app.settings import mail_setting, app_settings

conf = ConnectionConfig(
    MAIL_USERNAME=mail_setting.username,
    MAIL_PASSWORD=mail_setting.password,
    MAIL_FROM=mail_setting.from_email,
    MAIL_PORT=mail_setting.port,
    MAIL_SERVER=mail_setting.server,
    MAIL_TLS=mail_setting.tls,
    MAIL_SSL=mail_setting.ssl
)


class MailHelper:

    async def send_welcome_email(self, registration_data, user_email):
        await self.send_email(
            subject='Inscripción a II Carrera Virtual Runners Cúcuta',
            html_template="",
            recipents=[user_email],
            template_name='welcome.html',
            template_data=registration_data,
        )

    async def send_reset_password_email(self, recovery_password_data: dict, user_email: str):
        await self.send_email(
            subject='Runners Cúcuta: Recupera tu contraseña',
            html_template="",
            recipents=[user_email],
            template_name='reset_password.html',
            template_data=recovery_password_data,
        )

    async def send_registration_email(self, registration_data, user_email):
        await self.send_email(
            subject='Confirmación de inscripción a II Carrera Virtual Runners Cúcuta',
            html_template="",
            recipents=[user_email],
            template_name='confirmed_payment.html',
            template_data=registration_data,
        )

    @classmethod
    async def send_email(cls, subject, html_template, recipents, template_name=None, template_data=None):
        if template_data:
            template_data["app_url"] = app_settings.url
        if template_name:
            env = Environment(
                loader=PackageLoader('app', 'templates/email'),
                autoescape=select_autoescape(['html', 'xml', 'txt'])
            )
            template = env.get_template(template_name)
            html_template = template.render(**template_data)

        message = MessageSchema(
            subject=subject,
            recipients=recipents,
            html=html_template.encode('utf-8'),
            subtype="html",
        )
        fm = FastMail(conf)
        await fm.send_message(message)
