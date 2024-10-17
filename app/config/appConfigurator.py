
# config/appConfigurator.py

import logging


from app.core.shared.exceptions import ApiHandlerException
from app.core.auth import AuthHandlers

class AppConfigurator:
   """Classe para configurar o aplicativo Flask durante a inicialização."""

   def __init__(self, app):
      self.app = app
      logging.info("0: AppConfigurator.__init__()")

   def configure(self):
      with self.app.app_context():
            # Configurações e manipuladores
            ApiHandlerException(self.app)
            #AuthHandlers(self.app)