# Usa a imagem oficial do Debian como base
FROM debian:bullseye

# Define variáveis de ambiente para evitar interações durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Atualiza os pacotes e instala MySQL Server e Bash
RUN apt-get update && apt-get install -y \
    python3\
    python3-flask\
    bash\
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app

# Copia o script de inicialização do MySQL
COPY ./app/* /app

# porta http para uso API
#EXPOSE 33306