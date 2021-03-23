from fastapi_mail import ConnectionConfig, MessageSchema, FastMail

from app.settings import mail_setting

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
        welcome_email_template = """
        <p>
            Hola {first_name},
        </p>
        <p>
            Runnerscucuta te da la bienvenida a esta gran fiesta running. Te confirmamos el 
            registro de tus datos correctamente, solo te falta un paso, registra el 
            soporte del pago y te haremos llegar la confirmación final de la inscripción. 
        </p>
        <p> Estos son tus datos de inscripción: </p>
        - Nombres: {full_name} <br>
        - Télefono: {phone} <br>
        - Dirección: {address} <br>
        - Identificación: {document_number} <br>
        <p>
            Somos un equipo de running aficionado y recreativo, que fomenta hábitos de vida saludable e 
            impulsa la cultura running en nuestra región. <br />
            Nuestro lema: <strong>#YOCORROPORSALUD. </strong> <br />
            Te invitamos a que revises nuestras redes sociales instagram y Facebook @runnerscucuta y Runnerscucuta.com
        </p>
        """.format(**registration_data)
        await self.send_email(
            subject='Inscripción a II Carrera Virtual Runner Cúcuta',
            html_template=welcome_email_template,
            recipents=[user_email]
        )

    async def send_registration_email(self, registration_data, user_email):
        welcome_email_template = """
        <p>
            Hola {first_name},
        </p>
        <p>
            Runnerscucuta <strong>TE CONFIRMA</strong> que tu registro de datos personales y pago de la inscripción fue 
            exitosa y nuevamente te damos la bienvenida a esta gran fiesta running y 
            deseamos que sea tu mejor experiencia.
        </p>
        <p>
            Te invitamos a seguir generando cultura running y hábitos de vida saludable con los que te rodean 
            y recuerda  #YOCORROPORSALUD.
        </p>
        <p>
            Somos un equipo de running aficionado y recreativo, que fomenta hábitos de vida saludable e 
            impulsa la cultura running en nuestra región. <br />
            Nuestro lema: <strong> #YOCORROPORSALUD. </strong> <br />
            Te invitamos a que revises nuestras redes sociales instagram y Facebook @runnerscucuta y Runnerscucuta.com
        </p>
        """.format(**registration_data)
        await self.send_email(
            subject='Confirmación de inscripción a II Carrera Virtual Runner Cúcuta',
            html_template=welcome_email_template,
            recipents=[user_email]
        )

    @classmethod
    async def send_email(cls, subject, html_template, recipents):
        message = MessageSchema(
            subject=subject,
            recipients=recipents,  # List of recipients, as many as you can pass
            body=html_template,
            subtype="html"
        )
        fm = FastMail(conf)
        await fm.send_message(message)