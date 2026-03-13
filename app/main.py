from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import usuarios, tarefas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API", version="1.0.0")

# Configuração essencial para permitir que o Vue.js converse com o FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, colocaríamos "http://localhost:5173"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios.router)
app.include_router(tarefas.router)