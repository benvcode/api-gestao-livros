# livros/__init__.py

from .livro import Livro
from .livroRepository import LivroRepository
from .livroService import LivroService
from .livroViews import *
from .schemas import *


def livros_blueprints(app, BASE_API_URL):
   livros_views = LivrosApi.as_view("livros_api")
   
   app.add_url_rule(
      f"{BASE_API_URL}/livros",
      view_func=livros_views,
      methods=["GET", "POST"],
   )

   app.add_url_rule(
      f"{BASE_API_URL}/livros/<int:livro_id>",
      view_func=livros_views,
      methods=["GET", "PUT" "DELETE"],
   )
