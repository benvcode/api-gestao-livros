# exceptions/apiHandlerException.py

import logging
import re
from flask import Flask, jsonify
from flask_jwt_extended.exceptions import NoAuthorizationError
from sqlalchemy.exc import IntegrityError
from . import EntityNotFoundException, EntityUniqueViolationException

from marshmallow import ValidationError

class ApiHandlerException:
    def __init__(self, app):
        self.app = app
        self._register_error_handlers()

    def _register_error_handlers(self):
        """Registra manipuladores de erros personalizados.

        Captura e manipula exceções que ocorrem em qualquer parte da aplicação,
        fornecendo uma resposta consistente para erros específicos.
        """

        @self.app.errorhandler(ValidationError)
        def handle_marshmallow_validation_error(error):
            """Handle Marshmallow validation errors."""
            logging.error("Api Error - %s", error)
            return jsonify({"errors": str(error.messages)}), 400

        @self.app.errorhandler(EntityNotFoundException)
        def handle_entity_not_found(error):
            """Manipula a exceção quando uma entidade solicitada não é encontrada."""
            logging.error("Api Error - %s", error)
            return jsonify({"msg": str(error)}), 404

        @self.app.errorhandler(EntityUniqueViolationException)
        def handle_entity_unique_violation(error):
            """Handles exceptions when a uniqueness violation occurs."""
            logging.error("Api Error - %s", error)

            # Extract the field name from the error message
            field = extract_field_from_message(str(error))

            response = {
                "msg": f"Este {field} já existe. Experimente outro.",
                "field": field,
            }

            return jsonify(response), 409

        @self.app.errorhandler(NoAuthorizationError)
        def handle_missing_authorization_header(error):
            """Manipula a falta de cabeçalho de autorização"""
            logging.error("Api Error - %s", error)
            return (
                jsonify({"msg": str(error)}),
                401,
            )
