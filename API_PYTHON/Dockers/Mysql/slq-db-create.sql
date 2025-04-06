-- Criar o banco de dados
CREATE DATABASE Pi3;

-- Usar o banco de dados
USE Pi3;

-- Cria as tabelas
CREATE TABLE login (
    cpf VARCHAR(11) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    senha TEXT NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    PRIMARY KEY (cpf)
);

-- CPF será chave estrangeira vinda de Login
CREATE TABLE ponto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) NOT NULL,
    nome VARCHAR(100) NOT NULL,
    validado boolean NOT NULL DEFAULT FALSE,
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cpf) REFERENCES login(cpf) ON DELETE CASCADE
);

