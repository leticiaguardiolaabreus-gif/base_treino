from database.connection import get_connection

def install():
    connection = get_connection()

    try:
        # Criar tabela no banco de dados
        connection.execute("""CREATE TABLE IF NOT EXISTS bolos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, sabor TEXT NOT NULL, 
        feito BOOLEAN NOT NULL DEFAULT 0)""")

        cursor = connection.execute("""SELECT COUNT(*) FROM bolos""")
        total = cursor.fetchone()[0]

        if total == 0:
            connection.execute("""INSERT INTO bolos (nome, sabor, feito) VALUES (?,?,?)"""
             ("sonho de verão", "morango com baunilha", False),)
        
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")