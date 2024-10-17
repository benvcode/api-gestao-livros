# autorService.py

from sqlalchemy.exc import IntegrityError

from app.core.shared.utils import SingletonMeta
from app.core.shared.exceptions import EntityUniqueViolationException, EntityNotFoundException

from .autor import Autor
from .autorRepository import AutorRepository

class AutorService(metaclass=SingletonMeta):
    def __init__(self):
        self.autor_repository = AutorRepository()

    def create(self, autor: Autor):
        try:
            logging.debug("0: AutorService().create()")

            autor_criado = self.autor_repository.save(autor)

            logging.info("1: AutorService.create()")
            return autor_criado

        except IntegrityError as ex:
            if "unique constraint" in str(ex.orig):
                logging.error("IntegrityError %s", ex.orig)
                raise EntityUniqueViolationException(ex.orig)

        except Exception as ex:
            logging.error("%s", ex)

    def get_all(self):
        return self.autor_repository.find_all()

    def get_by_id(self, autor_id):
        autor = self.autor_repository.find_by_id(autor_id)
        if autor is None:
            raise EntityNotFoundException(f"Autor com id {autor_id} não encontrado.")
        return user

    def update(self, novo_autor, autor_id):
        updated = self.user_repository.update(novo_autor, autor_id)
        if updated is None:
            raise EntityNotFoundException(f"Autor com id {autor_id} não encontrado.")
        return updated

    def delete(self, autor_id):
        return self.user_repository.delete(autor_id)