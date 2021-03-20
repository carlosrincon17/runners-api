from fastapi_mail import ConnectionConfig, MessageSchema, FastMail

conf = ConnectionConfig(
    MAIL_USERNAME="runnerscucuta.noreply@gmail.com",
    MAIL_PASSWORD="Runners123",
    MAIL_FROM="runnerscucuta.noreply@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False
)


class MailHelper:

    async def send_welcome_email(self, registration_data, user_email):
        welcome_email_template = """
        <p>Hola {first_name},</p>
        
        <p> La inscripción a la II Carrera Virtual Runner Cúcuta ha sido exitosa. Estos son tus datos de inscripción: </p>
        - Nombres: {full_name} <br>
        - Télefono: {phone} <br>
        - Dirección: {address} <br>
        - Identificación: {document_number} <br>
        
        <p>Gracias!!</p>
        """.format(**registration_data)
        await self.send_email(
            subject='Inscripción a II Carrera Virtual Runner Cúcuta',
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
