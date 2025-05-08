import jwt
import datetime 
from jwt import ExpiredSignatureError, InvalidTokenError
# def auth_encode(usuario,cpf,cargo):
#     token = jwt.encode({
#         "nome":usuario,
#         "cpf":cpf,
#         "cargo":cargo
#         },key="123456789",algorithm="HS256")
#     return token
def auth_encode(dados,exp_time=30):
    tempo_expiracao = datetime.now() + datetime.timedelta(minutes=exp_time)
    token = jwt.encode({
        "nome": dados["usuario"],
        "cpf": dados["cpf"],
        "cargo": dados["cargo"],
        "exp":tempo_expiracao
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


