# Usa a imagem oficial do Debian como base
FROM debian:bullseye

# Define variáveis de ambiente 
ENV DEBIAN_FRONTEND=noninteractive
ENV MYSQL_ROOT_PASSWORD=p@55.0rd

# instala MySQL Server e Bash
RUN apt-get update && apt-get install -y \
    mariadb-server \
    bash \
    && rm -rf /var/lib/apt/lists/*

# Copia o script de inicialização do MySQL
COPY "slq-db-create.sql" /docker-entrypoint-initdb.d/

# Expõe a porta padrão do MySQL
EXPOSE 3306

# Inicia o MySQL
CMD ["mysqld"]
