# autorCreateSchema.py

from marshmallow import Schema, fields, validate, post_load
from app.core.shared.utils import ValidationUtils
from ..autor import Autor

class AutorCreateSchema(Schema):
   nome = fields.Str(
      required=True,
         error_messages={"required": "O campo nome é obrigatório."}
   )

   email = fields.Str(
      validate=[ValidationUtils.email()]
   )

   @post_load
   def make_autor(self, data, **kwargs):
      """Desserializar dados para uma instância Autor"""
      return Autor(**data)
