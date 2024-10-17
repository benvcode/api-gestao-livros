# autores/__init__.py

from .autor import Autor
from .autorRepository import AutorRepository
from .autorService import AutorService
from .autorViews import *
from .schemas import *

def autores_blueprints(app, BASE_API_URL):
   autores_views = AutoresApi.as_view("autores_api")

   app.add_url_rule(
      f"{BASE_API_URL}/autores",
      view_func=autores_views,
      methods=["GET", "POST"],
   )

   app.add_url_rule(
      f"{BASE_API_URL}/autores/<int:autor_id>",
      view_func=autores_views,
      methods=["GET", "PUT" "DELETE"],
   )


