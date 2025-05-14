from flask import Flask, request, jsonify, make_response
#from itsdangerous import URLSafeTimedSerializer
from Auth.auth import auth_encode, auth_decode
import pymysql

from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'chave-secreta-supersegura'  # use uma real no ambiente de produção


db_config = {
    "host": "localhost",
    "user": "pIuser",
    "password": "pI123",
    "database": "db_PI"
}

CORS(app, supports_credentials=True)

# Rota de login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data.get('usuario')
    senha = data.get('senha')
    if not usuario or not senha:
        return jsonify({"erro": "Usuário e senha obrigatórios"}), 400
    try:
        connection = pymysql.connect(**db_config)  
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT cpf,senha,usuario,cargo FROM login WHERE usuario = %s", (usuario,))
            result = cursor.fetchone()
        if result and result["senha"] == senha:
            usuario_info = {
                "usuario": result["usuario"],
                "cpf": result["cpf"],
                "cargo": result["cargo"]
            }
            token = auth_encode(usuario_info)
            return jsonify({"token": token})
        else:
            return jsonify({"erro": "Usuário ou senha inválidos"}), 401
    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500

@app.route('/inserir_ponto', methods=['POST'])
def insert_ponto():
    try:
        data = request.json
        timestamp_app = data.get('timestamp')
        token_auth = data.get('Authenticator')
        dados_usuarios = auth_decode(token_auth)
        connection = pymysql.connect(**db_config)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO ponto (cpf, usuario, data_hora) VALUES (%s,%s,%s)", (dados_usuarios['cpf'],dados_usuarios['usuario'],timestamp_app))
            connection.commit()
            return jsonify({"message":{"cpf": dados_usuarios['cpf'],"usuario":dados_usuarios['usuario'],"timestamp":timestamp_app}})
    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500

@app.route("/get_pontos", methods=['POST'])
def get_pontos():
    data = request.json
    token_auth = data.get('Authenticator')
    dados_usuario = auth_decode(token_auth)
    connection = pymysql.connect(**db_config)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM ponto WHERE validado=0;")
        result = cursor.fetchall()
        return jsonify(result)

@app.route("/get_ponto", methods=['POST'])
def get_ponto():
    data = request.json
    token_auth = data.get('Authenticator')
    dados_usuario = auth_decode(token_auth)
    connection = pymysql.connect(**db_config)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM ponto WHERE usuario=%s;",dados_usuario["usuario"])
        result = cursor.fetchall()
        return jsonify(result)
    
@app.route("/set_ponto", methods=['POST'])
def validar_ponto():
    data=request.json
    token_auth = data.get("Authenticator")
    id_ponto = data.get("id")
    dados_usuario = auth_decode(token_auth)
    connection = pymysql.connect(**db_config)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("UPDATE ponto SET validado=1 WHERE id=%s;", id_ponto)
        connection.commit()
    return {"success":"Ponto inserido com sucesso"}


app.run(host='0.0.0.0', debug=True)