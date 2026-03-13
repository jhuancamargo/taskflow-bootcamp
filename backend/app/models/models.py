import enum
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.database import Base

# Definição dos Enums para restringir os valores aceitos no banco
class PrioridadeEnum(str, enum.Enum):
    baixa = "Baixa"
    media = "Média"
    alta = "Alta"

class StatusEnum(str, enum.Enum):
    a_fazer = "A Fazer"
    em_andamento = "Em Andamento"
    concluido = "Concluído"

# Entidade Usuário
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    funcao = Column(String, nullable=False)

    # Relacionamento: 1 Usuário tem N Tarefas
    tarefas = relationship("Tarefa", back_populates="responsavel", cascade="all, delete-orphan")

# Entidade Tarefa
class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    prioridade = Column(SQLEnum(PrioridadeEnum), default=PrioridadeEnum.media, nullable=False)
    prazo = Column(Date, nullable=True)
    status = Column(SQLEnum(StatusEnum), default=StatusEnum.a_fazer, nullable=False)
    
    # Chave Estrangeira ligando à tabela de usuários
    responsavel_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    # Relacionamento de volta para a classe Usuario
    responsavel = relationship("Usuario", back_populates="tarefas")