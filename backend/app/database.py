from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Porta 5433 para evitar conflito com Postgres local
SQLALCHEMY_DATABASE_URL = "postgresql://admin:adminpassword@localhost:5433/taskflow_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()