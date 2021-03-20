import pydantic


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "ACME API"
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "INFO"

    class Config(BaseSettings.Config):
        env_prefix = "API_"


class ThirdPartySettings(BaseSettings):
    trm_api: str

    class Config(BaseSettings.Config):
        env_prefix = "THIRD_PARTY_"


class MongoSettings(BaseSettings):
    uri: str
    database: str
    username: str
    password: str

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


api_settings = APISettings()
mongo_settings = MongoSettings()
third_party_settings = ThirdPartySettings()
