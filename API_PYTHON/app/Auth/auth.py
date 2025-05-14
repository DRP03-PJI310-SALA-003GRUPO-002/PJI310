import jwt
import datetime 
from jwt import ExpiredSignatureError, InvalidTokenError
import pytz


timezone_sp = pytz.timezone('America/Sao_Paulo')

def auth_encode(dados,exp_time=30):
    tempo_expiracao = datetime.datetime.now(timezone_sp) + datetime.timedelta(minutes=exp_time)
    token = jwt.encode({
        "usuario": dados["usuario"],
        "cpf": dados["cpf"],
        "cargo": dados["cargo"],
        "exp":tempo_expiracao
    }, key="123456789", algorithm="HS256")
    return token

# Gera refresh token (longa duração)
def refresh_token_encode(dados, exp_days=7):
    tempo_expiracao = datetime.datetime.now() + datetime.timedelta(days=exp_days)
    token = jwt.encode({
        "cpf": dados["cpf"],  # Apenas identificador essencial
        "exp": tempo_expiracao
    }, key="123456789", algorithm="HS256")
    return token


def auth_decode(token):
    try:
        userdados = jwt.decode(token,key="123456789",algorithms="HS256")
        return userdados
    except ExpiredSignatureError:
        return {"erro": "Token expirado"}
    except InvalidTokenError:
        return {"erro": "Token inválido"}


def gerar_novo_access_token(refresh_token):
    try:
        dados = jwt.decode(refresh_token, key="123456789", algorithms=["HS256"])
        # Normalmente você buscaria os dados completos do usuário a partir do CPF, mas aqui é simplificado
        novo_token = auth_encode({
            "usuario": "usuario_teste",  # Substitua com dados reais buscados
            "cpf": dados["cpf"],
            "cargo": "usuario"
        })
        return novo_token
    except ExpiredSignatureError:
        return {"erro": "Refresh token expirado"}
    except InvalidTokenError:
        return {"erro": "Refresh token inválido"}