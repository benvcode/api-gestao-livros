# config.py

from decouple import config

class Config(object):
    """Configurações comuns."""

    # SWAGGER = {
    #     "title": "API Gestão de Livros",
    #     "uiversion": 3,
    #     "description": "API documentation",
    #     "version": "1.0.0",
    # }


    PORT = config("PORT", default=5000, cast=int)
    SQLALCHEMY_DATABASE_SCHEMA = config("DATABASE_SCHEMA")
    BASE_API_URL = config("BASE_API_URL")
    API_KEY_STATIC = config("API_KEY_STATIC")

class DevConfig(Config):
    """Configurações de desenvolvimento local, para testes rápidos."""
    FLASK_ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = config("DATABASE_URI_LOCAL_DEV")

# Outras classes aqui ...

def get_config():
    env = config("FLASK_ENV")

    if env == "development":
       return "config.DevConfig"
    # Outras verificações aqui se necessário ...