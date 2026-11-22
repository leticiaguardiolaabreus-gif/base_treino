from database.connection import get_connection
from entities.entity import Bolo

class DAOEntity:

    def create(self, bolo):
        connection = get_connection()

        try:
            cursor = connection.execute("""INSERT INTO bolo (nome, sabor, feito) 
            VALUES (bolo.nome, bolo.sabor, bolo.feito)""")

            connection.commit()
            return cursor.lastrowid


        finally:
            connection.close()




    def find_all(self):
        connection = get_connection()
        try:
            cursor = connection.execute("SELECT * FROM bolo")
            lista = cursor.fetchall

            registros = []
            for registro in lista:
                bolo= Bolo()
                bolo.id= registro[0]
                bolo.nome = registro[1]
                bolo.sabor = registro[2]
                bolo.feito = bool(registro[3])

                registros.append(bolo)
            return registros

        finally:
            connection.close()

    def find_by_id(self, task_id):
        # Consultar pelo ID
        pass

    def update(self, task):
        # Atualizar
        pass

    def delete(self, task_id):
        # Excluir
        pass