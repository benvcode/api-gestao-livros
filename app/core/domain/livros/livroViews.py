# livroViews.py

from flask import request, jsonify
import logging

from app.core.shared.utils import BaseProtectedView, SchemaUtils
from .livroService import LivroService
from .schemas import LivroCreateSchema, LivroResponseSchema, LivroEditSchema

class LivrosApi(BaseProtectedView):
   def __init__(self):
      super().__init__()
      self.livro_service = LivroService()

   def post(self):
      livro_data = request.get_json()

      logging.debug("1: LivrosApi.post")

      livro = SchemaUtils.deserialize(LivroCreateSchema(), livro_data)

      livro_criado = self.livro_service.create(livro)
      
      logging.info("1: LivrosApi.post")

      # Retorna uma resposta com status 201 (CREATED) e corpo contendo os dados do livro.
      return jsonify(SchemaUtils.serialize(LivroResponseSchema(), livro_criado)), 201

   def get(self, livro_id=None):
      if livro_id:
            livro = self.livro_service.get_by_id(livro_id)
            # Retorna uma resposta com status 200 (OK) e o corpo contendo o livro
            return jsonify(SchemaUtils.serialize(LivroResponseSchema(), livro)), 200
      else:
            livros = self.livro_service.get_all()
            # Retorna uma resposta com status 200 (OK) e corpo contendo a lista de livros
            return jsonify(SchemaUtils.serialize(LivroResponseSchema(), livros)), 200

   def put(self, livro_id):
      """
      Atualiza um recurso existente com todos os campos fornecidos.

      Recomendações para o uso do método PUT:
            - Incluir todos os campos do recurso, mesmo aqueles que não serão modificados.
            - Usar valores mascarados para campos sensíveis que não devem ser alterados.
      """
      livro_data = request.get_json()

      novo_livro = SchemaUtils.deserialize(LivroEditSchema(), livro_data)

      self.livro_service.update(novo_livro, livro_id)

      # Retorna uma resposta com status 204 (No Content) indicando que o livro foi
      # atualizado com sucesso.
      return "", 204

   def delete(self, livro_id):
      self.livro_service.get_by_id(livro_id)

      # Retorna uma resposta com status 204 (No Content) indicando que o livro foi
      # deletado com sucesso.
      self.livro_service.delete(livro_id)
      return "", 204
