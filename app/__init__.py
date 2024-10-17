# app/__init__.py

import logging

from flask import Flask
from .config import AppConfigurator
from .extensions import init_extensions
from .core.domain import register_domain_blueprints

def create_app(config_class):
    """Cria e configura a instância do aplicativo Flask."""

    app = Flask(__name__)

    # Carrega Configuração do app
    app.config.from_object(config_class)

    # Inicializar  extensões
    init_extensions(app)

    #  Configurar o app
    configurator = AppConfigurator(app)
    configurator.configure()

    # Importar o módulo domain e registra os blueprints
    from .core import domain

    register_domain_blueprints(app)

    return app

