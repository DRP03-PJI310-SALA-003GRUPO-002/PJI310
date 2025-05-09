Execute o comando abaixo para instalar as depêndencias da aplicação, é necessário estar no diretorio app para isso

`pip install -r requirements.txt`

Após isso certifiquese que o docker esteja instalado em sua máquina. 

Caso já esteja instalado execute o comando no seu terminal para criar a rede pi_network

`docker network create --driver bridge pi_network`

Após isso execute o dentro estando dentro do diretorio Dockers dockercompose.yml 

`docker-compose up -d`

Para parar os containers use 

`docker-compose stop`