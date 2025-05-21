from flask import Flask, request, jsonify, make_response
#from itsdangerous import URLSafeTimedSerializer
from Auth.auth import auth_encode, auth_decode
from Functions.intervalo import obter_intervalo
import pymysql
import pytz

from dateutil import parser

from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'chave-secreta-supersegura'  # use uma real no ambiente de produção


db_config = {
    "host": "localhost",
    "user": "pIuser",
    "password": "pI123",
    "database": "db_PI"
}
timezone_sp = pytz.timezone('America/Sao_Paulo')

CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost"}})

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
        token_auth = data.get('token')
        dados_usuarios = auth_decode(token_auth)

        # Converte o timestamp ISO 8601 para datetime e formata
        dt_obj = parser.isoparse(timestamp_app).astimezone(timezone_sp)  # converte para timezone correto
        formatted_timestamp = dt_obj.strftime('%Y-%m-%d %H:%M:%S')       # formato compatível com MySQL

        connection = pymysql.connect(**db_config)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                "INSERT INTO ponto (cpf, usuario, data_hora) VALUES (%s, %s, %s)",
                (dados_usuarios['cpf'], dados_usuarios['usuario'], formatted_timestamp)
            )
            connection.commit()
            return jsonify({"message": {
                "cpf": dados_usuarios['cpf'],
                "usuario": dados_usuarios['usuario'],
                "timestamp": formatted_timestamp
            }})
    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500

@app.route("/get_user_ponto", methods=['POST'])
def get_ponto():
    data = request.json
    token_auth = data.get('token')
    dados_usuario = auth_decode(token_auth)
    
    mes = data.get('month') 
    ano = data.get('year') 
    begin,end = obter_intervalo(mes, ano)
    
    connection = pymysql.connect(**db_config)
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("SELECT * FROM ponto WHERE usuario=%s AND data_hora >= %s AND data_hora < %s;",(dados_usuario["usuario"],begin,end))
        result = cursor.fetchall()
        return jsonify(result)

@app.route("/get_user", methods=['POST'])
def get_user_info():
    data =request.json
    token_auth = data.get('token')
    dados_usuario = auth_decode(token_auth)
    return jsonify(dados_usuario), 200

    
@app.route("/set_ponto", methods=['POST'])
def validar_ponto():
    data=request.json
    token_auth = data.get("token")
    id_ponto = data.get("id")
    dados_usuario = auth_decode(token_auth)
    try:
        connection = pymysql.connect(**db_config)
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE ponto SET validado=1 WHERE id=%s;", id_ponto)
            connection.commit()
    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500
    return {"success":"Ponto inserido com sucesso"}

@app.route("/get_pontos_by_month", methods=['POST'])
def get_pontos_by_month():
    data = request.json
    token_auth = data.get('token')
    mes = data.get('month') 
    ano = data.get('year') 
    begin,end = obter_intervalo(mes, ano)
    dados_usuario = auth_decode(token_auth)
    try:
        connection = pymysql.connect(**db_config)  
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM ponto WHERE data_hora >= %s AND data_hora < %s",(begin,end))
            result = cursor.fetchall()
    except Exception as e:
            return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500
    return jsonify(result)




app.run(host='0.0.0.0', debug=True)










# @app.route("/get_pontos", methods=['POST'])
# def get_pontos():
#     data = request.json
#     token_auth = data.get('token')
#     dados_usuario = auth_decode(token_auth)
#     connection = pymysql.connect(**db_config)
#     with connection.cursor(pymysql.cursors.DictCursor) as cursor:
#         cursor.execute("SELECT * FROM ponto WHERE validado=0;")
#         result = cursor.fetchall()
#         return jsonify(result)
