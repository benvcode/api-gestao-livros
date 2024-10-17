# autor.py

from sqlalchemy.orm import relationship

from app.extensions import db
from app.core.domain.autores_livros import autor_livro 


class Autor(db.Model):
    __tablename__ = "autor"
    __table_args__ = {"schema": "gestao_livros"}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    # Outros atributos ....  

    # Relacionamento N:N entre Livro e Autor
    # A propriedade 'secondary' especifica a tabela de associação 'role_Livro' usada para
    # mapear a relação muitos-para-muitos.
    # A propriedade 'back_populates="livros"' indica que a relação é bidirecional:
    # A entidade Role pode acessar todas as Livro associadas a ela através do atributo 'livros'.
    livros = db.relationship(
        'Livro', secondary=autor_livro, back_populates='autores'
    )

  
  