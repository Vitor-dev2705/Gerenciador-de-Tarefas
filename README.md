# Gerenciador-de-Tarefas
API de Gerenciamento de Tarefas

# Tarefas API

O **Tarefas API** é um sistema de gerenciamento de tarefas baseado em **FastAPI**. A API permite criar, listar, atualizar, excluir e autenticar tarefas de forma simples e eficiente. Além disso, oferece integração com fontes externas para adicionar tarefas automaticamente.

Este projeto foi desenvolvido com o intuito de demonstrar como construir e gerenciar uma aplicação moderna de API RESTful, com autenticação via tokens JWT, operações CRUD e integração externa.

## Funcionalidades

- **Gerenciamento de tarefas**: O sistema permite a criação de tarefas, listagem das tarefas cadastradas, atualização do status de tarefas e a exclusão de tarefas.
- **Autenticação de usuários**: A API implementa autenticação baseada em tokens JWT, permitindo a autenticação e autorização seguras para interagir com as rotas protegidas.
- **Integração com fontes externas**: Existe uma rota específica para importar tarefas de fontes externas, por meio de um processo automatizado de **crawler**.
- **Operações CRUD completas**: O sistema implementa as operações básicas de criação, leitura, atualização e exclusão (CRUD) para gerenciar as tarefas.

## Como Usar

### 1. Pré-requisitos

Para usar o projeto, você precisa do seguinte:

- **Python 3.12 ou superior**.
- **Uvicorn** como servidor ASGI.
- **FastAPI** para a construção da API.
- **JWT (JSON Web Token)** para autenticação segura.

### 2. Instalação

Para rodar o projeto localmente, siga os seguintes passos:

1. **Clone o repositório**:
   Clone o repositório em seu computador:
   ```bash
   git clone <url-do-repositorio>

    Crie e ative um ambiente virtual: No terminal, execute os comandos:

python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate

Instale as dependências: Com o ambiente virtual ativado, instale as dependências necessárias:

pip install -r requirements.txt

Inicie o servidor: Execute o seguinte comando para iniciar o servidor de desenvolvimento:

    uvicorn src.app.main:app --reload

    Acesse a API: Depois que o servidor estiver em execução, a API estará disponível em http://localhost:8000.

3. Endpoints da API

A API oferece os seguintes endpoints principais:
3.1. Login e Autenticação

    POST /token: Realiza o login de um usuário e retorna um token JWT para autenticação.

    Para realizar o login, envie um POST para o endpoint /token com o nome de usuário e a senha:

    Exemplo de Requisição:

{
  "username": "admin",
  "password": "123456"
}

Resposta Esperada:

    {
      "access_token": "<seu-token-jwt>",
      "token_type": "bearer"
    }

    Credenciais de Exemplo:
        Usuário: admin
        Senha: 132456

    O token gerado deve ser usado em todas as requisições subsequentes para autenticar o usuário.

3.2. Gerenciamento de Tarefas

    POST /tarefas: Cria uma nova tarefa.

    Exemplo de Requisição:

{
  "titulo": "Estudar para o exame",
  "descricao": "Revisar todos os conceitos de Python.",
  "estado": "pendente"
}

Resposta Esperada:

{
  "id": 1,
  "titulo": "Estudar para o exame",
  "descricao": "Revisar todos os conceitos de Python.",
  "estado": "pendente",
  "data_criacao": "2025-01-10T12:34:56",
  "data_atualizacao": "2025-01-10T12:34:56"
}

GET /tarefas: Lista todas as tarefas cadastradas.

Exemplo de Requisição:

GET http://localhost:8000/tarefas

Resposta Esperada:

[
  {
    "id": 1,
    "titulo": "Estudar para o exame",
    "descricao": "Revisar todos os conceitos de Python.",
    "estado": "pendente",
    "data_criacao": "2025-01-10T12:34:56",
    "data_atualizacao": "2025-01-10T12:34:56"
  }
]

GET /tarefas/{task_id}: Recupera uma tarefa específica pelo seu id.

Exemplo de Requisição:

GET http://localhost:8000/tarefas/1

Resposta Esperada:

{
  "id": 1,
  "titulo": "Estudar para o exame",
  "descricao": "Revisar todos os conceitos de Python.",
  "estado": "pendente",
  "data_criacao": "2025-01-10T12:34:56",
  "data_atualizacao": "2025-01-10T12:34:56"
}

PUT /tarefas/{task_id}: Atualiza os dados de uma tarefa existente.

Exemplo de Requisição:

{
  "titulo": "Estudar para o exame - Atualizado",
  "descricao": "Revisar tópicos avançados de Python.",
  "estado": "em andamento"
}

Resposta Esperada:

{
  "id": 1,
  "titulo": "Estudar para o exame - Atualizado",
  "descricao": "Revisar tópicos avançados de Python.",
  "estado": "em andamento",
  "data_criacao": "2025-01-10T12:34:56",
  "data_atualizacao": "2025-01-10T14:45:00"
}

DELETE /tarefas/{task_id}: Deleta uma tarefa pelo id.

Exemplo de Requisição:

DELETE http://localhost:8000/tarefas/1

Resposta Esperada:

{
  "message": "Tarefa deletada com sucesso"
}

POST /tarefas/crawler: Importa tarefas de fontes externas via um processo de crawler.

Exemplo de Requisição:

POST http://localhost:8000/tarefas/crawler

Resposta Esperada:

    {
      "message": "Tarefas importadas com sucesso"
    }

4. Autenticação

Para interagir com as rotas protegidas da API (como a criação e manipulação de tarefas), você precisará autenticar um usuário utilizando um token JWT. A autenticação é feita através do endpoint /token, que retorna um token que deve ser enviado nas requisições subsequentes, no cabeçalho Authorization, no formato Bearer <token>.

Exemplo de cabeçalho para requisições autenticadas:

Authorization: Bearer <seu-token-jwt>

5. Diretório __pycache__

O diretório __pycache__ contém os arquivos compilados em bytecode do Python (arquivos .pyc), que são gerados automaticamente para acelerar a execução do código. O Python cria esse diretório sempre que um script Python é executado, e ele não precisa ser manipulado manualmente. É seguro ignorá-lo ou até removê-lo, pois o Python irá recriá-lo automaticamente conforme necessário.
Estrutura do Projeto

O projeto está organizado da seguinte maneira:

    src/: Contém todos os arquivos de código-fonte da aplicação, incluindo:
        app/main.py: Contém a instância da API e as rotas principais.
        app/auth.py: Lógica de autenticação e geração de tokens JWT.
        app/models.py: Modelos de dados e esquemas para as tarefas.
        app/crud.py: Funções para manipulação dos dados das tarefas.
        app/crawler.py: Funções para buscar tarefas externas.

    __pycache__/: Diretório gerado automaticamente pelo Python para armazenar arquivos compilados (bytecode).

    requirements.txt: Lista de dependências necessárias para rodar o projeto.



    Esse `README.md` contém todas as etapas de como configurar o ambiente, como fazer o login, como interagir com a API e detalhes técnicos sobre o projeto. Ele também explica como o login deve ser feito, com o usuário `vitor` e a senha `teles`, além de fornecer exemplos completos das requisições e respostas.
