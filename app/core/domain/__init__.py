# app/core/domain/__init__.py

from .livros import *
from .autores import *
from .autores_livros import *

def register_domain_blueprints(app):
    BASE_API_URL = app.config["BASE_API_URL"]

    autores_blueprints(app, BASE_API_URL)
    livros_blueprints(app, BASE_API_URL) 
