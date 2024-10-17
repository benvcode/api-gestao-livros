from marshmallow import Schema, fields, validate, post_load
from app.core.shared.utils import ValidationUtils
from app.core.domain.autores.schemas import AutorCreateSchema

from app.core.domain.autores.autor import Autor
from ..livro import Livro

class LivroCreateSchema(Schema):
   isbn = fields.Str(
      required=True,
   )

   titulo = fields.Str(
      required=True,
      error_messages={"required": "O campo título é obrigatório."}
   )

   num_paginas = fields.Int(
      required=True,
   )

   autores = fields.List(fields.Nested(AutorCreateSchema), required=True, error_messages={"required": "Pelo menos um autor é obrigatório."})

   @post_load
   def make_livro(self, data, **kwargs):
      """Desserializa dados para uma instância Livro"""
      autores_data = data.pop('autores', [])
      livro = Livro(**data)

      # Associa autores ao livro
      for autor_data in autores_data:
         if isinstance(autor_data, dict):
               # Se autor_data for um dicionário, criamos uma instância de Autor
               autor = Autor(**autor_data)
         elif isinstance(autor_data, Autor):
               # Se autor_data já for uma instância de Autor, reutilizamos
               autor = autor_data
         else:
               raise TypeError(f"Tipo inválido de autor_data: {type(autor_data)}")

         livro.autores.append(autor)

      # O SQLAlchemy cuidará de inserir os dados do autor na tabela autor e também fará as entradas na tabela de associação autor_livro.
      return livro