import flask 
import json
from connectMysql import conectar_bd, mysqli

'''API
	FUNÇÃO PAGINA DE LOGIN
		boolValidaLogin(cpf,senha)
'''
# Validar login
def boolValidaLogin(cpf, senha):
    conexao = conectar_bd()
    if not conexao:
        return False  # Se não conectar ao banco, retorna falso

    try:
        cursor = conexao.cursor()
        consulta = "SELECT cpf FROM login WHERE cpf = %s AND senha = %s"
        cursor.execute(consulta, (cpf, senha))
        resultado = cursor.fetchone()
        
        if resultado: # Verifica se consta algo em resultado 
            if cpf in resultado: # Verifica se cpf está em resultado
                return True
        return False
    
    except mysqli.connector.Error as erro:
        print(f"Erro na consulta: {erro}")
        return False
    finally:
        cursor.close()
        conexao.close()


'''
	FUNÇÃO PAGINA DE PONTO DO FUNCIONÁRIO
		setInseripontoFuncionario(id funcionario, data e hora)
		logoutSession()

	
	FUNÇÃO TELA PAGINA DO GESTOR
		getFuncionarios() retorna list funcionarios[nome, cpf]
		getFuncionarioPontos() retorna list pontosFuncionario[id funcionario, data e hora]
		setValidaPontoFuncionario(id ponto, bool validador)
		logoutSession() '''