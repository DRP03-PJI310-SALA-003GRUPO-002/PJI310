from flask import Flask, request, jsonify, make_response
#from itsdangerous import URLSafeTimedSerializer
from Auth.auth import auth_encode, auth_decode
import pymysql


from flask_cors import CORS



app = Flask(__name__)
app.secret_key = 'chave-secreta-supersegura'  # use uma real no ambiente de produção

#serializer = URLSafeTimedSerializer(app.secret_key)

db_config = {
    "host": "localhost",
    "user": "pIuser",
    "password": "pI123",
    "database": "db_PI"
}

CORS(app, supports_credentials=True)

# @app.route('/inserir_ponto', methods=['POST'])
# def teste():
#     try:
#         usuario = autenticar_cookie(request)
#         data = request.json
#         timestamp_app = data.get('timestamp')
#         connection = pymysql.connect(**db_config)
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT cpf FROM login WHERE nome = %s", (usuario,))
#             cpf = cursor.fetchone()
#             cursor.execute("INSERT INTO ponto (cpf, nome, data_hora) VALUES (%s,%s,%s)", (cpf,usuario,timestamp_app))
#             connection.commit()
#             return jsonify({"message":{"cpf": cpf,"nome":usuario,"timestamp":timestamp_app}})
#     except Exception as e:
#         return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500
# @app.route('/inserir_ponto', methods=['POST'])

@app.route('/inserir_ponto', methods=['POST'])
def teste():
    try:
        data = request.json
        timestamp_app = data.get('timestamp')
        connection = pymysql.connect(**db_config)
        with connection.cursor() as cursor:
            cursor.execute("SELECT cpf FROM login WHERE nome = %s", (usuario,))
            cpf = cursor.fetchone()
            cursor.execute("INSERT INTO ponto (cpf, nome, data_hora) VALUES (%s,%s,%s)", (cpf,usuario,timestamp_app))
            connection.commit()
            return jsonify({"message":{"cpf": cpf,"nome":usuario,"timestamp":timestamp_app}})
    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500

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
            cursor.execute("SELECT cpf,senha,nome,cargo FROM login WHERE nome = %s", (usuario,))
            result = cursor.fetchone()
        if result and result["senha"] == senha:
            usuario_info = {
                "usuario": result["nome"],
                "cpf": result["cpf"],
                "cargo": result["cargo"]
            }
            token = auth_encode(usuario_info)

        #with connection.cursor() as cursor:
            #cursor.execute("SELECT senha FROM login WHERE nome = %s", (usuario,))
            #result = cursor.fetchone()

        # if result and result[1] == senha:
            #token = serializer.dumps(usuario)  # gera um token assinado com o nome do usuário
            # cpf = result[0]
            # senha = result[1]
            # nome = result[2]
            # cargo = result[3]
            # token = auth_encode(nome,cpf,cargo)

            #response = make_response(jsonify({"mensagem": "Login bem-sucedido"}))
            #response.set_cookie("auth_token", token, httponly=True, samesite='Strict')
            return jsonify({"token": token})
        else:
            return jsonify({"erro": "Usuário ou senha inválidos"}), 401

    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500

# Middleware para proteger rotas
# def autenticar_cookie(request):
#     token = request.cookies.get('auth_token')
#     if not token:
#         return None
#     try:
#         usuario = serializer.loads(token, max_age=3600)  # válido por 1 hora
#         return usuario
#     except Exception:
#         return None

# Rota protegida
@app.route('/dados')
def dados_protegidos():
    data = request.json
    token = data.get('Authenticator')
    x = auth_decode(token)
    return jsonify(x)
    #usuario = autenticar_cookie(request)
    # if not usuario:
    #     return jsonify({"erro": "Não autorizado"}), 401

    # return jsonify({"mensagem": f"Bem-vindo, {usuario}. Aqui estão seus dados protegidos."})
    #return


app.run(host='0.0.0.0', debug=True)