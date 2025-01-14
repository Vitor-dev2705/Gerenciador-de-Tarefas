from pydantic import BaseModel, validator
from datetime import datetime
from typing import Optional
from typing import Literal
from fastapi import HTTPException

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: Optional[str] = None
    estado: Literal["pendente", "em andamento", "concluída"]  # Apenas esses valores são permitidos
    data_criacao: datetime
    data_atualizacao: datetime

    @validator("estado")
    def validar_estado(cls, valor):
        if valor not in ["pendente", "em andamento", "concluída"]:
            raise HTTPException(
                status_code=400,
                detail=f"Estado '{valor}' não é um valor válido. Os valores aceitos são 'pendente', 'em andamento' e 'concluída'."
            )
        return valor

class TarefaCriar(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    estado: Literal["pendente", "em andamento", "concluída"]  # Apenas esses valores são permitidos

    @validator("estado")
    def validar_estado(cls, valor):
        if valor not in ["pendente", "em andamento", "concluída"]:
            raise HTTPException(
                status_code=400,
                detail=f"Estado '{valor}' não é um valor válido. Os valores aceitos são 'pendente', 'em andamento' e 'concluída'."
            )
        return valor
