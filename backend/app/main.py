from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

# ADICIONA ESTA LINHA ANTES DO create_all
from app.models import models

import app.routers.usuarios as usuarios_router
import app.routers.tarefas as tarefas_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(usuarios_router.router)
app.include_router(tarefas_router.router)

@app.get("/")
def root():
    return {"message": "API Rodando"}