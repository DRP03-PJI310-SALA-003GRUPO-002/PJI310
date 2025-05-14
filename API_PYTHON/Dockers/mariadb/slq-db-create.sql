-- Criar o banco de dados
CREATE DATABASE IF NOT EXISTS db_PI;

-- Usar o banco de dados
USE db_PI;

-- INICIO TABELAS
CREATE TABLE login (
    cpf VARCHAR(11) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    senha TEXT NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    PRIMARY KEY (cpf)
);

-- CPF será chave estrangeira vinda de Login
CREATE TABLE ponto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(11) NOT NULL,
    usuario VARCHAR(100) NOT NULL,
    validado boolean NOT NULL DEFAULT FALSE,
    data_hora TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cpf) REFERENCES login(cpf) ON DELETE CASCADE
);

-- Inserir usuários apenas se ainda não existirem
INSERT IGNORE INTO login (cpf, usuario, senha, cargo) VALUES
('12345678901', 'joao', '123456', 'ti'),
('23456789012', 'maria', 'senha123', 'ti'),
('34567890123', 'carlos', 'abc123', 'gerente_ti'),
('45678901234', 'ana', 'qwerty', 'gerente_ti'),
('56789012345', 'paulo', '123abc', 'rh');
