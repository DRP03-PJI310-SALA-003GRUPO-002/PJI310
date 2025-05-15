DROP DATABASE db_PI;
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


INSERT INTO ponto (cpf, usuario, validado, data_hora) VALUES
-- Dentro do intervalo solicitado: 26/04/2025 a 25/05/2025
('12345678901', 'joao', TRUE, '2025-04-30 08:15:00'),
('23456789012', 'maria', FALSE, '2025-05-10 17:45:00'),

-- Fora do intervalo (anteriores)
('34567890123', 'carlos', TRUE, '2025-04-20 09:00:00'),
('45678901234', 'ana', TRUE, '2025-04-15 18:00:00'),
('56789012345', 'paulo', FALSE, '2025-03-28 07:50:00'),
('12345678901', 'joao', TRUE, '2025-02-26 12:00:00'),
('23456789012', 'maria', TRUE, '2025-01-05 08:30:00'),

-- Fora do intervalo (posteriores)
('34567890123', 'carlos', FALSE, '2025-05-26 09:15:00'),
('45678901234', 'ana', TRUE, '2025-06-01 16:45:00'),
('56789012345', 'paulo', TRUE, '2025-06-05 10:10:00'),

-- Datas variadas aleatórias
('12345678901', 'joao', FALSE, '2024-12-12 14:20:00'),
('23456789012', 'maria', TRUE, '2024-11-03 07:00:00'),
('34567890123', 'carlos', TRUE, '2024-10-15 11:11:00'),
('45678901234', 'ana', FALSE, '2024-09-25 09:59:00'),
('56789012345', 'paulo', TRUE, '2024-08-19 16:40:00'),
('12345678901', 'joao', TRUE, '2024-07-04 13:05:00'),
('23456789012', 'maria', FALSE, '2024-06-08 06:55:00'),
('34567890123', 'carlos', TRUE, '2024-05-23 18:30:00'),
('45678901234', 'ana', TRUE, '2024-04-17 20:20:00'),
('56789012345', 'paulo', FALSE, '2024-03-10 12:34:00');