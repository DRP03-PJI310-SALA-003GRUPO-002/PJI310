import mysql.connector as mysqli

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conexao = mysqli.connector.connect(
            host="localhost",
            user="root",
            password="p@55.0rd",
            database="db_PI"
        )
        return conexao
    except mysqli.connector.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None

