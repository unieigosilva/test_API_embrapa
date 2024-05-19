# Adicionar o diretório raiz do projeto ao sys.path
import sys
sys.path.append('./app/')


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_app.models import Base, metadata
from config import Config_AC  # Importando configurações

# URL de conexão com o banco de dados. Pode ser substituída pela URL do seu banco de dados.
database_path = Config_AC.get('database_path')
DATABASE_URL = f"sqlite:///{database_path}"


# Cria o engine do SQLAlchemy, que é a interface principal com o banco de dados
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine) 

# Cria uma fábrica de sessões para interação com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter uma nova sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

