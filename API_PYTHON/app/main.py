from flask import Flask, request, jsonify, make_response
from itsdangerous import URLSafeTimedSerializer
import pymysql

app = Flask(__name__)
app.secret_key = 'chave-secreta-supersegura'  # use uma real no ambiente de produção

serializer = URLSafeTimedSerializer(app.secret_key)

db_config = {
    "host": "db",
    "user": "pIuser",
    "password": "pI123",
    "database": "db_PI"
}

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
        with connection.cursor() as cursor:
            cursor.execute("SELECT senha FROM login WHERE nome = %s", (usuario,))
            result = cursor.fetchone()

        if result and result[0] == senha:
            token = serializer.dumps(usuario)  # gera um token assinado com o nome do usuário
            response = make_response(jsonify({"mensagem": "Login bem-sucedido"}))
            response.set_cookie("auth_token", token, httponly=True, samesite='Strict')
            return response
        else:
            return jsonify({"erro": "Usuário ou senha inválidos"}), 401

    except Exception as e:
        return jsonify({"erro": f"Erro no servidor: {str(e)}"}), 500

# Middleware para proteger rotas
def autenticar_cookie(request):
    token = request.cookies.get('auth_token')
    if not token:
        return None
    try:
        usuario = serializer.loads(token, max_age=3600)  # válido por 1 hora
        return usuario
    except Exception:
        return None

# Rota protegida
@app.route('/dados')
def dados_protegidos():
    usuario = autenticar_cookie(request)
    if not usuario:
        return jsonify({"erro": "Não autorizado"}), 401

    return jsonify({"mensagem": f"Bem-vindo, {usuario}. Aqui estão seus dados protegidos."})
