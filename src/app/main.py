from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from datetime import datetime
from src.app.auth import create_access_token, decode_token, oauth2_scheme
from src.app.models import Tarefa, TarefaCriar
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()

# Banco de Dados Simulado (em memória)
tarefas: List[Tarefa] = []
proximo_id = 1

# Função para verificar o token de autenticação
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    return payload

# Função simulada para buscar tarefas externas (por exemplo, de um crawler)
def buscar_tarefas_externas():
    # Esta função simula a busca de tarefas externas, como um crawler faria.
    return [
        {"title": "Tarefa Externa 1", "completed": False},
        {"title": "Tarefa Externa 2", "completed": True},
    ]


# Rota para criar tarefa
@app.post("/tarefas", response_model=Tarefa)
def criar_tarefa(tarefa: TarefaCriar, token: str = Depends(oauth2_scheme)):
    global proximo_id
    nova_tarefa = Tarefa(
        id=proximo_id,
        titulo=tarefa.titulo,
        descricao=tarefa.descricao,
        estado=tarefa.estado,
        data_criacao=datetime.now(),
        data_atualizacao=datetime.now()
    )
    tarefas.append(nova_tarefa)
    proximo_id += 1
    return nova_tarefa

# Rota para listar tarefas
@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas(token: str = Depends(oauth2_scheme)):
    return tarefas

# Rota para pegar uma tarefa específica
@app.get("/tarefas/{task_id}", response_model=Tarefa)
def obter_tarefa(task_id: int, token: str = Depends(oauth2_scheme)):
    for tarefa in tarefas:
        if tarefa.id == task_id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para atualizar uma tarefa
@app.put("/tarefas/{task_id}", response_model=Tarefa)
def atualizar_tarefa(task_id: int, tarefa_atualizada: TarefaCriar, token: str = Depends(oauth2_scheme)):
    for tarefa in tarefas:
        if tarefa.id == task_id:
            tarefa.titulo = tarefa_atualizada.titulo
            tarefa.descricao = tarefa_atualizada.descricao
            tarefa.estado = tarefa_atualizada.estado
            tarefa.data_atualizacao = datetime.now()  # Atualiza a data de modificação
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para deletar uma tarefa
@app.delete("/tarefas/{task_id}", response_model=dict)
def deletar_tarefa(task_id: int, token: str = Depends(oauth2_scheme)):
    global tarefas
    for tarefa in tarefas:
        if tarefa.id == task_id:
            tarefas.remove(tarefa)
            return {"detail": "Tarefa deletada com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

# Rota para login e obtenção de token
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Substitua esta validação com a lógica real de autenticação
    if form_data.username == "admin" and form_data.password == "123456":
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )

# Rota para adicionar tarefas via crawler (ou fonte externa)
@app.post("/tarefas/crawler", response_model=List[Tarefa])
def adicionar_tarefas_via_crawler(user: dict = Depends(get_current_user)):
    global proximo_id

    # Busca as tarefas externas usando o crawler
    tarefas_externas = buscar_tarefas_externas()

    # Adiciona as tarefas externas ao banco de dados interno
    novas_tarefas = []
    for tarefa_externa in tarefas_externas:
        nova_tarefa = Tarefa(
            id=proximo_id,
            titulo=tarefa_externa.get("title", "Tarefa Sem Título"),
            descricao="Tarefa importada de fonte externa.",
            estado="pendente" if not tarefa_externa.get("completed") else "concluída",
            data_criacao=datetime.now(),
            data_atualizacao=datetime.now()
        )
        tarefas.append(nova_tarefa)
        novas_tarefas.append(nova_tarefa)
        proximo_id += 1

    return novas_tarefas
