from datetime import datetime
from typing import Optional
from src.app.models import Tarefa, TarefaCriar, Usuario
from src.app.auth import get_password_hash, verify_password

# Banco de dados em memória (apenas para exemplo)
tarefas = []  # Lista para armazenar tarefas
proximo_id = 1  # ID autoincrementado para as tarefas

# Simulação de banco de dados de usuários
# Senha 'teles' está armazenada com hash para maior segurança
usuarios_db = {
    "user1": {"username": "vitor", "password": get_password_hash("teles")}
}

# Função para criar uma tarefa
def criar_tarefa(tarefa: TarefaCriar) -> Tarefa:
    global proximo_id
    nova_tarefa = Tarefa(
        id=proximo_id,
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        estado="pendente",  # Definir estado inicial como "pendente"
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now()
    )
    tarefas.append(nova_tarefa)
    proximo_id += 1
    return nova_tarefa

# Função para verificar as credenciais do usuário
def verificar_usuario(username: str, password: str) -> Optional[Usuario]:
    """
    Verifica se o usuário e senha fornecidos são válidos.
    """
    user = usuarios_db.get(username)
    if user and verify_password(password, user["password"]):
        return user  # Retorna o usuário se a senha for correta
    return None  # Retorna None se as credenciais forem inválidas
