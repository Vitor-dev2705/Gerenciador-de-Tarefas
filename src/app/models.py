from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    estado: str
    data_criacao: datetime
    data_atualizacao: datetime

class TarefaCriar(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    estado: str
