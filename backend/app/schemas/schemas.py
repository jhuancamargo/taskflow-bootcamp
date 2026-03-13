from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional, List
from app.models.models import PrioridadeEnum, StatusEnum

# ==========================================
# SCHEMAS DE TAREFAS
# ==========================================
class TarefaBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    prioridade: PrioridadeEnum = PrioridadeEnum.media
    prazo: Optional[date] = None
    status: StatusEnum = StatusEnum.a_fazer
    responsavel_id: int

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    titulo: Optional[str] = None
    descricao: Optional[str] = None
    prioridade: Optional[PrioridadeEnum] = None
    prazo: Optional[date] = None
    status: Optional[StatusEnum] = None
    responsavel_id: Optional[int] = None

class TarefaResponse(TarefaBase):
    id: int

    class Config:
        from_attributes = True  # Permite que o Pydantic leia objetos do SQLAlchemy

# ==========================================
# SCHEMAS DE USUÁRIOS
# ==========================================
class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    funcao: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioResponse(UsuarioBase):
    id: int
    tarefas: List[TarefaResponse] = []  # Retorna as tarefas atreladas ao usuário

    class Config:
        from_attributes = True