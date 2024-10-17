from marshmallow import Schema, fields, post_dump
from app.core.domain.autores.schemas import AutorResponseSchema

class LivroResponseSchema(Schema):
    id = fields.Int()
    isbn = fields.Str()
    titulo = fields.Str()
    num_paginas = fields.Int()
    autores = fields.List(fields.Nested(AutorResponseSchema(only=["nome"]))) 

