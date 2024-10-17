# autorEditSchema.py

from marshmallow import Schema, fields, validate, post_load
from app.core.shared.utils import ValidationUtils
from ..autor import Autor

class AutorEditSchema(Schema):
   """Esse schema pode ser usado tanto para:
      1. Response: Os dados retornados na resposta são utilizados em requisições PUT
      2. Request: Para valida e carregar os dados do cliente em requisições PUT
   """

   id = fields.Int(required=True)  
   nome = fields.Str(
      required=True,
      validate=[
            validate.Length(min=1, error="O nome não pode ser vazio.")
      ]
   )

   email = fields.Str(
      validate=[ValidationUtils.email()]
   )

   @post_load  # Chamado no momento da desserialização usando 'load'
   def make_autor(self, data, **kwargs):
      return Autor(**data)
