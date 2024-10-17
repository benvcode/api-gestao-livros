# autor_livro.py

from sqlalchemy.orm import relationship

from app.extensions import db


# Definindo a tabela de associação muitos-para-muitos entre Autor e Livro.
# Esta tabela não possui atributos adicionais, então não é necessário criar uma
# classe separada. Será referenciada nas classes Autor e Livros usando 'secondary'.

autor_livro = db.Table(
    'autor_livro', db.metadata,
    db.Column('autor_id', db.Integer, db.ForeignKey(
        'gestao_livros.autor.id'), primary_key=True),
    db.Column('livro_id', db.Integer, db.ForeignKey(
        'gestao_livros.livro.id'), primary_key=True),
    schema='gestao_livros'
)

