# autorResponseSchema.py

from marshmallow import Schema, fields, post_dump

class AutorResponseSchema(Schema):
    id = fields.Int()
    nome = fields.Str()
    email = fields.Str() 
