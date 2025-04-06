from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

from Model.Ponto import Ponto
from Model.Usuario import User


app = Flask(__name__)

# Configurações do MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:p@55.0rd@localhost/db_PI"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config["SECRET_KEY"] = "sua_chave_secreta"


# Rota de login e geração de token JWT
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Credenciais inválidas"}), 401

    # Gera token JWT
    token = jwt.encode({
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, app.config["SECRET_KEY"], algorithm="HS256")

    return jsonify({"token": token})

# Middleware simples de autenticação
def token_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Token vem do cabeçalho Authorization: Bearer <token>
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token ausente"}), 401

        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.get(data["user_id"])
        except Exception as e:
            return jsonify({"message": "Token inválido ou expirado", "error": str(e)}), 401

        return f(current_user, *args, **kwargs)
    return decorated



# Rota de registro
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Usuário e senha são obrigatórios"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "Usuário já existe"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário registrado com sucesso"}), 201