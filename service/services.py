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
        return self.repository.find_all()

    def get(self, bolo_id):
        resultado = self.repository.find_by_id(bolo_id)
        if not resultado:
            print("Não encontrado")
        return resultado

    def update(self, task_id, title, description):
        pass

    def delete(self, task_id):
        pass