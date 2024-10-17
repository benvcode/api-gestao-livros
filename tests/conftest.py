# conftest.py

import pytest
import logging

from app import create_app
from app.extensions import db

logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True, scope="session")
def test_app(request):
    config_class = request.param
    app = create_app(config_class=config_class)

    with app.app_context():
        if config_class == "config.DevConfig":
            # SQLite em memória não suporta esquemas
            # Remover o schema 'deltruck' para garantir que os testes funcionem corretamente
            for table in db.metadata.sorted_tables:
                if table.schema == "gestao_livros":
                    table.schema = None

        #db.drop_all()  #  Apagar banco de dado para cada teste

        db.create_all()  # Cria todas as tabelas apenas uma vez
        
        yield app

        db.session.remove()  # Remove a sessão, mas não apaga o banco de dados

    logger.info("conftest.test_app(): test_client fixture is being used")
