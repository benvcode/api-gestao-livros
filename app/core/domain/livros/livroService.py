# livroService.py

from sqlalchemy.exc import IntegrityError
import logging

from app.core.shared.utils import SingletonMeta
from app.core.shared.exceptions import EntityUniqueViolationException, EntityNotFoundException

from .livro import Livro
from .livroRepository import LivroRepository

class LivroService(metaclass=SingletonMeta):
    def __init__(self):
        self.livro_repository = LivroRepository()

    def create(self, livro: Livro):
        try:
            logging.debug("0: LivroService().create()")

            livro_criado = self.livro_repository.save(livro)

            logging.info("1: LivroService.create()")
            return livro_criado

        except IntegrityError as ex:
            if "unique constraint" in str(ex.orig):
                logging.error("IntegrityError %s", ex.orig)
                raise EntityUniqueViolationException(ex.orig)

        except Exception as ex:
            logging.error("%s", ex)
            raise ex  # Re-raise the exception for further handling

    def get_all(self):
        return self.livro_repository.find_all()  # Assumindo que o método find_all() está implementado

    def get_by_id(self, livro_id):
        livro = self.livro_repository.find_by_id(livro_id)
        if livro is None:
            raise EntityNotFoundException(f"Livro com id {livro_id} não encontrado.")
        return livro

    def update(self, novo_livro, livro_id):
        updated = self.livro_repository.update(novo_livro, livro_id)
        if updated is None:
            raise EntityNotFoundException(f"Livro com id {livro_id} não encontrado.")
        return updated

    def delete(self, livro_id):
        return self.livro_repository.delete(livro_id)
