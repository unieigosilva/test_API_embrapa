# app/sql_app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, metadata
from app.config import Config_AC  # Importando configurações

database_path = Config_AC.get('database_path')
DATABASE_URL = f"sqlite:///{database_path}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)  # Assegura que todas as tabelas estão carregadas conforme a reflexão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
