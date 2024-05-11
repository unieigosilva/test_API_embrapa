# sql_app/test_query.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.sql_app.models import Production
from app.sql_app.base import Base
from app.config import Config_AC

database_path = Config_AC.get('database_path')

# Configuração do banco de dados

DATABASE_URL = f"sqlite:///{database_path}"
engine = create_engine(DATABASE_URL, echo=True)  # O 'echo=True' é para ver as consultas no terminal
SessionLocal = sessionmaker(bind=engine)

def test_query():
    session = SessionLocal()
    try:
        # Realiza uma consulta simples
        production_data = session.query(Production).all()
        for data in production_data:
            print(f"ID: {data.id}, Produto: {data.produto}")
    finally:
        session.close()

if __name__ == "__main__":
    test_query()
