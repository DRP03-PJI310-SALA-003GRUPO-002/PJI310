# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Configurar variaveis de ambiente
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Instale o cron
RUN apt-get update && apt-get install -y cron \
nano \
procps \
iputils-ping
RUN pip install --upgrade pip setuptools

# Defina o diretorio de trabalho no contaiainer
WORKDIR /Myapp

# Copie os arquivos de dependencias para o container
COPY requirements.txt .

# Instale as dependencias do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie o cogo-fonte do seu projeto para o container
COPY . .

# Copie o script de ponto de entrada
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Exponha a porta que a aplicacao Flask usara
EXPOSE 5000

# Comando para rodar o script de ponto de entrada
CMD ["/entrypoint.sh"]
