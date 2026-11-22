from repository.dao_entity import DAOEntity
from entities.entity import Bolo

class Services:

    def __init__(self, repository):
        self.repository = repository

    def create(self, nome, sabor):

        if not nome or not nome.strip():
            raise ValueError("Erro")
        if not sabor or not sabor.strip():
            raise ValueError("Erro")

        bolo = Bolo()
        bolo.nome = nome.strip()
        bolo.sabor = sabor.strip()
        bolo.feito = False
        bolo.id = self.repository.create(bolo)
        return bolo

    def list(self):
        pass

    def get(self, task_id):
        pass

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass