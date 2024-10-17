# shared/utils/validationUtis.py

from marshmallow import validate, ValidationError

class ValidationUtils:
    @staticmethod
    def email():
        return validate.Email(
            error="O endereço de e-mail fornecido não é válido."
        )
    