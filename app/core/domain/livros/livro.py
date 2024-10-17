# livro.py

from sqlalchemy.orm import relationship
from app.core.domain.autores_livros import autor_livro 

from app.extensions import db


class Livro(db.Model):
    __tablename__ = "livro"
    __table_args__ = {"schema": "gestao_livros"}
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False, unique=True)
    titulo = db.Column(db.String, nullable=False)
    num_paginas = db.Column(db.Integer, nullable=False)
    # Outros atributos ....   

    # Relacionamento N:N entre Livro e Autor
    # A propriedade 'secondary' especifica a tabela de associação 'autor_livro' usada para
    # mapear a relação muitos-para-muitos.
    # A propriedade 'back_populates="autores"' indica que a relação é bidirecional:
    # A entidade Livro pode acessar todas as Autors associadas a ela através do atributo 'autores'.
    autores = db.relationship(
        'Autor', secondary=autor_livro, back_populates='livros'
    )
