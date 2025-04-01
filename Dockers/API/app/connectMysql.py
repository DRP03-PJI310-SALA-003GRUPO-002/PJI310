import mysql.connector as mysqli

# Função para conectar ao banco de dados
def conectar_bd():
    try:
        conexao = mysqli.connector.connect(
            host="localhost",     # Altere para o host do seu banco
            user="seu_usuario",   # Altere para seu usuário
            password="sua_senha", # Altere para sua senha
            database="seu_banco"  # Altere para seu banco
        )
        return conexao
    except mysqli.connector.Error as erro:
        print(f"Erro ao conectar ao banco: {erro}")
        return None

