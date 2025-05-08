import jwt
# def auth_encode(usuario,cpf,cargo):
#     token = jwt.encode({
#         "nome":usuario,
#         "cpf":cpf,
#         "cargo":cargo
#         },key="123456789",algorithm="HS256")
#     return token
def auth_encode(dados):
    token = jwt.encode({
        "nome": dados["usuario"],
        "cpf": dados["cpf"],
        "cargo": dados["cargo"]
    }, key="123456789", algorithm="HS256")
    return token

def auth_decode(token):
    userdados = jwt.decode(token,key="123456789",algorithms="HS256")
    return userdados

