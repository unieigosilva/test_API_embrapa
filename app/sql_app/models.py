# Importa a biblioteca SQLAlchemy e a base de dados declarativa do arquivo database.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, text
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import  sql_app  # Importar o novo dicionário do arquivo config.py

Base = declarative_base()
metadata = MetaData()

database_path = sql_app['database_path']
DATABASE_URL = f"sqlite:///{database_path}"
#engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Usando reflexão para carregar a tabela e especificando explicitamente a chave primária
class Production(Base):
    __table__ = Table('producao', metadata, 
                      Column('id', Integer, primary_key=True),   # Explicitamente declarando 'id' como chave primária
                      autoload_with=engine)

    @staticmethod
    def get_production_by_year(year):
        session = SessionLocal()
        try:
            # Usando aspas corretas para SQL identifier quoting em SQLite
            sql_query = text(f"""SELECT produto, "{year}" as quantidade FROM producao""")
            result = session.execute(sql_query).fetchall()
            session.close()
            return [{"Produto": row[0], "Quantidade (L.)": row[1]} for row in result]
        except Exception as e:
            session.close()
            raise e

# Usando reflexão para carregar a tabela e especificando explicitamente a chave primária
class Commercialization(Base):
    __table__ = Table('comercializacao', metadata, 
                      Column('id', Integer, primary_key=True),
                      autoload_with=engine)

    @staticmethod
    def get_commercialization_by_year(year):
        session = SessionLocal()
        try:
            sql_query = text(f"""SELECT produto, "{year}" as quantidade FROM comercializacao""")
            result = session.execute(sql_query).fetchall()
            session.close()
            return [{"Produto": row[0], "Quantidade (L.)": row[1]} for row in result]
        except Exception as e:
            session.close()
            raise e

class Processing:
    @staticmethod
    def get_data_by_category_and_year(category: str, year: int):
        table_name = sql_app['processing'].get(category)
        if not table_name:
            raise ValueError("Categoria inválida para processamento")
        with SessionLocal() as session:
            query = text(f"SELECT cultivar, \"{year}\" FROM {table_name}")
            result = session.execute(query).fetchall()
            return [{"Cultivar": row[0], "Quantidade (Kg)": row[1]} for row in result]

class Importation:
    @staticmethod
    def get_data_by_category_and_year(category: str, year: int):
        table_name = sql_app['import'].get(category)
        if not table_name:
            raise ValueError("Categoria inválida para importação")
        with SessionLocal() as session:
            query = text(f"SELECT País, \"{year}\" as quantidade, \"{year}.1\" as valor FROM {table_name}")
            result = session.execute(query).fetchall()
            return [{"Países": row[0], "Quantidade (Kg)": row[1], "Valor (US$)": row[2]} for row in result]

class Exportation:
    @staticmethod
    def get_data_by_category_and_year(category: str, year: int):
        table_name = sql_app['export'].get(category)
        if not table_name:
            raise ValueError("Categoria inválida para exportação")
        with SessionLocal() as session:
            query = text(f"SELECT País, \"{year}\" as quantidade, \"{year}.1\" as valor FROM {table_name}")
            result = session.execute(query).fetchall()
            return [{"Países": row[0], "Quantidade (Kg)": row[1], "Valor (US$)": row[2]} for row in result]
