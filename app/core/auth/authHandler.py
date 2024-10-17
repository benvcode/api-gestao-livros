# core/decorators/auth.py

from flask import request, jsonify
from functools import wraps
from flask import request, jsonify, current_app

class AuthHandlers:
    def __init__(self, app):
        self.app = app
        self._register_before_requests()

    def _register_before_requests(self):
      """Registra o manipulador before_equest."""

      @self.app.before_request
      def check_api_auth():
          """Verifica a chave de API para rotas que não são de visualização."""
          if request.method in ['POST', 'PUT', 'DELETE']:
              api_key = request.headers.get("X-API-KEY")
              if api_key != current_app.config["API_KEY_STATIC"]:
                  return jsonify({"msg": "Chave de API inválida"}), 401