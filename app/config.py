import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "postgresql://admin:adminpassword@localhost:5432/my_db",
    )
    SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    FLASK_ENV = os.getenv("FLASK_ENV", "development")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:adminpassword@localhost:5432/test_db"
    TESTING = True
    SQLALCHEMY_ECHO = False
