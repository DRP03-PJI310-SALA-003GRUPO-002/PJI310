#API session
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuração do banco de dados (SQLite para simplicidade)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configuração de sessão (usando cookies no lado do cliente)
app.config["SECRET_KEY"] = "sua_chave_secreta_segura"
app.config["SESSION_TYPE"] = "filesystem"  # Alternativa: "redis" para produção
app.config["SESSION_PERMANENT"] = False  # Sessão expira ao fechar o navegador
app.config["SESSION_USE_SIGNER"] = True  # Protege contra manipulação de cookies
Session(app)

# Inicializa o banco de dados
db = SQLAlchemy(app)

# Modelo do Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Criar tabelas no banco (executar uma vez antes de rodar a API)
with app.app_context():
    db.create_all()

# Rota de Registro
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

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

# Rota de Login (Criação da Sessão)
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Credenciais inválidas"}), 401

    # Armazena o usuário na sessão
    session["user_id"] = user.id
    session["username"] = user.username

    return jsonify({"message": "Login realizado com sucesso!"}), 200

# Rota para verificar se o usuário está autenticado
@app.route("/session", methods=["GET"])
def check_session():
    if "user_id" in session:
        return jsonify({"message": f"Usuário autenticado: {session['username']}"}), 200
    return jsonify({"message": "Usuário não autenticado"}), 401

# Rota Protegida (apenas para usuários logados)
@app.route("/protected", methods=["GET"])
def protected():
    if "user_id" not in session:
        return jsonify({"message": "Acesso negado"}), 403
    return jsonify({"message": f"Bem-vindo, {session['username']}!"}), 200

# Rota de Logout (Destruir Sessão)
@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Logout realizado com sucesso!"}), 200

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(debug=True)
