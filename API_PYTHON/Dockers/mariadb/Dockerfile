FROM mariadb:latest

# Copia o script de criação para o diretório de inicialização do MariaDB
COPY slq-db-create.sql /docker-entrypoint-initdb.d/

# Variáveis de ambiente
ENV MARIADB_ROOT_PASSWORD=p@55w.rd
ENV MARIADB_DATABASE=db_PI
ENV MARIADB_USER=pIuser
ENV MARIADB_PASSWORD=pI123