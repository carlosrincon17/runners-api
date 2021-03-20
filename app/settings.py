import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


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


api_settings = APISettings()
db_settings = DbSettings()
