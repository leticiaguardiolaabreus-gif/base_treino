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

    def find_by_id(self, bolo_id):
        connection = get_connection()
        try:
            cursor = connection.execute("SELECT * FROM bolo WHERE id =?" (bolo_id,))
            registo = cursor.fetchone()
                
            bolo= Bolo()
            bolo.id= registro[0]
            bolo.nome = registro[1]
            bolo.sabor = registro[2]
            bolo.feito = bool(registro[3])
            return bolo
        finally:
            connection.close()


    def update(self, bolo):
        connection = get_connection()
        try:
            connection.execute("""UPDATE bolo SET nome = ?, sabor = ?, feito = ? WHERE id= ?"""
            , (bolo.nome, bolo.sabor, bolo.feito), bolo.id)
            connection.commit()
        except:
            connection.close()


    def delete(self, task_id):
        # Excluir
        pass