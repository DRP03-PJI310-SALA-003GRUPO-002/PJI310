# Usa a imagem oficial do Debian 12
FROM debian:bookworm 

# Define variáveis de ambiente para evitar interações durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e instala MySQL Server e Bash
RUN apt-get update && apt-get install -y \
    python3\
    python3-flask\
    #flask_sqlalchemy\
    bash\
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app

# Copia o script de inicialização do MySQL
COPY ./app/* /app

CMD ["tail", "-f", "/dev/null"]


# porta http para uso API
#EXPOSE 33306
