from marshmallow import Schema, fields, validate, post_load
from app.core.shared.utils import ValidationUtils
from ..livro import Livro

class LivroEditSchema(Schema):
   """Esse schema pode ser usado tanto para:
      1. Response: Os dados retornados na resposta são utilizados em requisições PUT
      2. Request: Para validar e carregar os dados do cliente em requisições PUT
   """

   id = fields.Int(required=True)

   isbn = fields.Str(
      required=True,
   )

   titulo = fields.Str(
   )

   num_paginas = fields.Int(
      required=True,
   )

   @post_load  # Chamado no momento da desserialização usando 'load'
   def make_livro(self, data, **kwargs):
      return Livro(**data)
