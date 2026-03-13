from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Tarefa, Usuario
from app.schemas.schemas import TarefaCreate, TarefaResponse, TarefaUpdate

router = APIRouter(
    prefix="/tarefas",
    tags=["Tarefas"]
)

@router.post("", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: TarefaCreate, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == tarefa.responsavel_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    
    nova_tarefa = Tarefa(**tarefa.model_dump())
    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)
    return nova_tarefa

@router.get("", response_model=List[TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return db.query(Tarefa).all()

@router.put("/{tarefa_id}", response_model=TarefaResponse)
def atualizar_tarefa(tarefa_id: int, tarefa_up: TarefaUpdate, db: Session = Depends(get_db)):
    db_tarefa = db.query(Tarefa).filter(Tarefa.id == tarefa_id).first()
    if not db_tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
    
    dados = tarefa_up.model_dump(exclude_unset=True)
    for key, value in dados.items():
        setattr(db_tarefa, key, value)
    
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa