import mysql.connector
from mysql.connector import Error

def testar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='pIuser',
            password='pI123',
            database='db_PI'
        )
        if conexao.is_connected():
            print("Conexão com o banco de dados bem-sucedida!")
            return True
    except Error as erro:
        print(f"Falha ao conectar ao banco de dados: {erro}")
        return False
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

testar_conexao()