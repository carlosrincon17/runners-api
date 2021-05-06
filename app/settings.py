import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = "runners.env"


class APISettings(BaseSettings):
    title: str = "Runners API"
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "INFO"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class DbSettings(BaseSettings):
    database: str = ''
    username: str = ''
    password: str = ''
    host: str = ''
    port: int = 5432

    class Config(BaseSettings.Config):
        env_prefix = "DB_"


class FileSettings(BaseSettings):
    path: str = ''

    class Config(BaseSettings.Config):
        env_prefix = "FILES_"


class JwtSettings(BaseSettings):
    algorithm: str = ''
    secret_key: str = ''
    access_token_expire_minutes: int

    class Config(BaseSettings.Config):
        env_prefix = "JWT_"


class MailSettings(BaseSettings):
    username: str = ''
    password: str = ''
    from_email: str = ''
    port: int = 0
    server: str = ''
    tls: bool = False
    ssl: bool = False

    class Config(BaseSettings.Config):
        env_prefix = "MAIL_"


api_settings = APISettings()
db_settings = DbSettings()
file_settings = FileSettings()
jwt_setting = JwtSettings()
mail_setting = MailSettings()
