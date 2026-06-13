# Guia do Usuário - Projeto Barbearia

Este guia ensina como executar o sistema de agendamentos da Barbearia.

## Pré-requisitos
* Docker e Docker Compose instalados na máquina.
* Git instalado.

## Como baixar o projeto
1. Clone o repositório:
   `git clone [LINK_DO_SEU_GITHUB]`
2. Entre na pasta:
   `cd barbearia-atividade5`

## Como configurar o .env
1. Copie o arquivo de exemplo:
   `cp .env.example .env`
2. Edite o arquivo .env com suas credenciais do banco de dados.

## Como subir os containers
Execute o comando:
`sudo docker compose up -d`

## Como acessar o sistema
Abra o navegador e acesse: `http://IP_DA_AWS:5000`

## Como parar o sistema
No diretório do projeto, execute:
`sudo docker compose down`
