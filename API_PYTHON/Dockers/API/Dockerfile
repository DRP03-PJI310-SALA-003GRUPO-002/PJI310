FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /opt/app

# Copia o diretório 'app' da estrutura local para o contêiner
COPY ./Dockers/API/app /opt/app

# Instala dependências, se houver requirements.txt
RUN pip install --no-cache-dir flask

# Comando para manter o contêiner ativo
CMD ["tail", "-f", "/dev/null"]
