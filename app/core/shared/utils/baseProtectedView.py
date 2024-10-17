# shared/utils/baseProtectedView.py

from flask.views import MethodView
from flask_jwt_extended import jwt_required

class BaseProtectedView(MethodView):
    """Classe base para views que requerem autenticação e autorização"""

    def __init__(self):
        self.decorators = [
            jwt_required(),
        ]
