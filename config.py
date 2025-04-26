import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY = config("SECRET_KEY")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database/dev.db")


class ProdConfig(Config):
    pass


class TestConfig(Config):
    pass
