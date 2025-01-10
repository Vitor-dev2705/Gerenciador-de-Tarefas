# Gerenciador-de-Tarefas
API de Gerenciamento de Tarefas

Tarefas API

Este projeto é uma API desenvolvida com FastAPI para gerenciar tarefas, com funcionalidades de criação, listagem, atualização, exclusão e integração com fontes externas (crawler). Também implementa autenticação usando tokens Bearer e paginação nas respostas de listagem de tarefas.
Tecnologias

    FastAPI: Framework para construção de APIs.
    SQLite: Banco de dados para persistência (não implementado neste código, mas indicado como uma melhoria futura).
    OAuth2: Sistema de autenticação com tokens Bearer.
    Requests: Para fazer requisições HTTP a fontes externas.
    Pydantic: Para modelagem de dados.

Funcionalidades

    Autenticação: Login com nome de usuário e senha para gerar um token Bearer.
    CRUD de Tarefas:
        Criar, listar, atualizar e excluir tarefas.
        Listagem com paginação.
    Integração com Fontes Externas (Crawler): Buscar tarefas de uma API externa e adicioná-las ao sistema.
    Paginação: Funcionalidade de paginação para limitar o número de tarefas retornadas.

Instalação
1. Clone o repositório

Primeiro, clone o repositório em sua máquina local:

git clone https://github.com/Vitor-dev2705/Gerenciador-de-Tarefas.git
cd Gerenciador-de-Tarefas

2. Instale as dependências

Crie um ambiente virtual e instale as dependências necessárias:

python -m venv venv
source venv/bin/activate  # Para sistemas Unix/macOS
venv\Scripts\activate     # Para sistemas Windows
pip install -r requirements.txt

Se não houver um arquivo requirements.txt, você pode instalar as dependências manualmente:

pip install fastapi uvicorn requests

3. Executar a API

Para rodar o servidor da API, execute o seguinte comando:

uvicorn main:app --reload

O servidor estará disponível em http://localhost:8000.
Uso da API
Autenticação

Antes de fazer qualquer requisição nas rotas protegidas, é necessário obter um token de autenticação. Para isso, faça uma requisição POST para /token com o nome de usuário e senha.

Exemplo de corpo da requisição para login (usando cURL ou Postman):

POST /token

{
  "username": "admin",
  "password": "123456"
}

Resposta:

{
  "access_token": "seu_token_aqui",
  "token_type": "bearer"
}

Utilize o token retornado em uma requisição Authorization como Bearer <seu_token_aqui>.
Endpoints

    Criar Tarefa

POST /tarefas

Corpo da requisição:

{
  "titulo": "Tarefa Exemplo",
  "descricao": "Descrição da tarefa",
  "estado": "pendente"
}

Resposta:

{
  "id": 1,
  "titulo": "Tarefa Exemplo",
  "descricao": "Descrição da tarefa",
  "estado": "pendente",
  "data_criacao": "2025-01-10T10:00:00",
  "data_atualizacao": "2025-01-10T10:00:00"
}

    Listar Tarefas com Paginação

GET /tarefas?skip=0&limit=10

Resposta:

[
  {
    "id": 1,
    "titulo": "Tarefa Exemplo",
    "descricao": "Descrição da tarefa",
    "estado": "pendente",
    "data_criacao": "2025-01-10T10:00:00",
    "data_atualizacao": "2025-01-10T10:00:00"
  }
]

    Obter Tarefa Específica

GET /tarefas/{task_id}

Exemplo:

GET /tarefas/1

Resposta:

{
  "id": 1,
  "titulo": "Tarefa Exemplo",
  "descricao": "Descrição da tarefa",
  "estado": "pendente",
  "data_criacao": "2025-01-10T10:00:00",
  "data_atualizacao": "2025-01-10T10:00:00"
}

    Atualizar Tarefa

PUT /tarefas/{task_id}

Corpo da requisição:

{
  "titulo": "Tarefa Atualizada",
  "descricao": "Nova descrição",
  "estado": "concluída"
}

Resposta:

{
  "id": 1,
  "titulo": "Tarefa Atualizada",
  "descricao": "Nova descrição",
  "estado": "concluída",
  "data_criacao": "2025-01-10T10:00:00",
  "data_atualizacao": "2025-01-10T12:00:00"
}

    Deletar Tarefa

DELETE /tarefas/{task_id}

Exemplo:

DELETE /tarefas/1

Resposta:

{
  "detail": "Tarefa deletada com sucesso"
}

    Adicionar Tarefas via Crawler

POST /tarefas/crawler?filtro_completadas=true

Resposta:

[
  {
    "id": 2,
    "titulo": "Tarefa Importada",
    "descricao": "Importada via crawler",
    "estado": "concluída",
    "data_criacao": "2025-01-10T10:30:00",
    "data_atualizacao": "2025-01-10T10:30:00"
  }
]


    Esse `README.md` contém todas as etapas de como configurar o ambiente, como fazer o login, como interagir com a API e detalhes técnicos sobre o projeto. Ele também explica como o login deve ser feito, com o usuário `admin` e a senha `123456`, além de fornecer exemplos completos das requisições e respostas.
