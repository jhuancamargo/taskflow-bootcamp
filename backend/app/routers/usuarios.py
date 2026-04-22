from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.models import Usuario
from app.schemas.schemas import UsuarioCreate, UsuarioResponse

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuários"]
)

@router.post("", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="E-mail já registrado.")

    novo_usuario = Usuario(**usuario.dict())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return {
        "id": novo_usuario.id,
        "nome": novo_usuario.nome,
        "email": novo_usuario.email,
        "funcao": novo_usuario.funcao,
        "tarefas": []
    }

@router.get("", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return [
        {
            "id": u.id,
            "nome": u.nome,
            "email": u.email,
            "funcao": u.funcao,
            "tarefas": []
        }
        for u in usuarios
    ]