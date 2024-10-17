# autorRepository.py

from app.extensions import db

from app.core.shared.utils import BaseRepository

from .autor import Autor

class AutorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Autor)
