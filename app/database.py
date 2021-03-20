from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings import db_settings

SQLALCHEMY_DATABASE_URL = "postgresql://{username}:{password}@{host}:{port}/{database}".format(
    username=db_settings.username,
    password=db_settings.password,
    database=db_settings.database,
    host=db_settings.host,
    port=db_settings.port
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

