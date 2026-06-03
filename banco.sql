-- Script de estrutura para o projeto Atividade 4
CREATE DATABASE IF NOT EXISTS barbearia_da_hora;
USE barbearia_da_hora;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    senha VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS agendamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    servico VARCHAR(100),
    data_agendamento VARCHAR(20),
    horario VARCHAR(10)
);