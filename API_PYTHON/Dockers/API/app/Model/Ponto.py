from app.main import db

class Ponto(db.Model):
    __tablename__ = "ponto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cpf = db.Column(db.String(11), db.ForeignKey("login.cpf", ondelete="CASCADE"), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    validado = db.Column(db.Boolean, nullable=False, default=False)
    data_hora = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())