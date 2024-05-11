
# app/sql_app/models.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, text
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config import Config_AC   # Supondo que Config_AC já está definido em config.py


Base = declarative_base()
metadata = MetaData()

database_path = Config_AC.get('database_path')
DATABASE_URL = f"sqlite:///{database_path}"
#engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Usando reflexão para carregar a tabela e especificando explicitamente a chave primária
class Production(Base):
    __table__ = Table('producao', metadata, 
                      Column('id', Integer, primary_key=True),  # Explicitamente declarando 'id' como chave primária
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
        table_mapping = {
            "viniferas": "Processamento_viniferas",
            "americanas_hibridas": "Processamento_americanas_hibridas",
            "uvas_mesa": "Processamento_uvas_mesa",
            "sem_classificacao": "Processamento_sem_classificacao"
        }
        table_name = table_mapping.get(category)
        if not table_name:
            raise ValueError("Categoria inválida para processamento")
        with SessionLocal() as session:
            query = text(f"SELECT cultivar, \"{year}\" FROM {table_name}")
            result = session.execute(query).fetchall()
            return [{"Cultivar": row[0], "Quantidade (Kg)": row[1]} for row in result]
        
class Importation:
    @staticmethod
    def get_data_by_category_and_year(category: str, year: int):
        table_mapping = {
            "vinhos_mesa": "Importacao_vinhos_mesa",
            "espumantes": "Importacao_espumantes",
            "uvas_frescas": "Importacao_uvas_frescas",
            "uvas_passas": "Importacao_uvas_passas",
            "suco_uva": "Importacao_suco_uva"
        }
        table_name = table_mapping.get(category)
        if not table_name:
            raise ValueError("Categoria inválida para importação")
        with SessionLocal() as session:
            query = text(f"SELECT País, \"{year}\" as quantidade, \"{year}.1\" as valor FROM {table_name}")
            result = session.execute(query).fetchall()
            return [{"Países": row[0], "Quantidade (Kg)": row[1], "Valor (US$)": row[2]} for row in result]

class Exportation:
    @staticmethod
    def get_data_by_category_and_year(category: str, year: int):
        table_mapping = {
            "vinhos_mesa": "Exportacao_vinhos_mesa",
            "espumantes": "Exportacao_espumantes",
            "uvas_frescas": "Exportacao_uvas_frescas",
            "suco_uva": "Exportacao_suco_uva"
        }
        table_name = table_mapping.get(category)
        if not table_name:
            raise ValueError("Categoria inválida para exportação")
        with SessionLocal() as session:
            query = text(f"SELECT País, \"{year}\" as quantidade, \"{year}.1\" as valor FROM {table_name}")
            result = session.execute(query).fetchall()
            return [{"Países": row[0], "Quantidade (Kg)": row[1], "Valor (US$)": row[2]} for row in result]