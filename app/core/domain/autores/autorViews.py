# autorViews.py

from flask import request, jsonify
import logging

from app.core.shared.utils import BaseProtectedView, SchemaUtils
from .autorService import AutorService
from .schemas import AutorCreateSchema, AutorResponseSchema,  AutorEditSchema

class AutoresApi(BaseProtectedView):
   def __init__(self):
      super().__init__()
      self.autor_service = AutorService()

   def post(self):
      autor_data = request.get_json()

      logging.debug("1: AutorsApi.post")

      autor = SchemaUtils.deserialize(AutorCreateSchema(), autor_data)

      autor_criado = self.autor_service.create(autor)

      logging.info("1: AutorsApi.post")

      # retorna uma resposta com status 201 (CREATED) e corpo contendo os dados do autor.
      return jsonify(SchemaUtils.serialize(AutorResponseSchema(), autor_criado)), 201
   
   def get(self, autor_id=None):
      if autor_id:
         autor = self.autor_service.get_by_id(autor_id)
         # Retorna uma resposta com status 200 (OK) e o corpo contendo o autor
         return jsonify(SchemaUtils.serialize(AutorResponseSchema(), autor)), 200

      else:
         autores = self.autor_service.get_all()
         # Retorna uma resposta com status 200 (OK) e corpo contendo a lista de autores
         return jsonify(SchemaUtils.serialize(AutorResponseSchema(), autores)), 200

      # Retorna uma resposta com status 200 (OK) e corpo contendo o autor.
      return jsonify(SchemaUtils.serialize(AutorEditSchema(), autor)), 200

   def put(self, autor_id):
      """
      Atualiza um recurso existente com todos os campos fornecidos.

      Recomendações para o uso do método PUT:
         - Incluir todos os campos do recurso, mesmo aqueles que não serão modificados.
         - Usar valores mascarados para campos sensíveis que não devem ser alterados.
      """
      autor_data = request.get_json()

      novo_autor = SchemaUtils.deserialize(AutorEditSchema(), autor_data)

      self.autor_service.update(novo_autor, autor_id)

      # Retorna uma resposta com status 204 (No Contect) indicando que o usuário foi
      # actualizado com sucesso.
      return "", 204


   def delete(self, autor_id):
      self.autor_service.get_by_id(autor_id)

      # Retorna uma resposta com status 204 (No Contect) indicando que o usuário foi
      # deletado com sucesso.
      return "", 204
