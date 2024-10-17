# livroRepository.py

from app.extensions import db

from app.core.shared.utils import BaseRepository

from .livro import Livro


class LivroRepository(BaseRepository):
    def __init__(self):
        super().__init__(Livro)
