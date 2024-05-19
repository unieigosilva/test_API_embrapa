import sqlite3  # Importa o módulo sqlite3 para trabalhar com o banco de dados SQLite
from contextlib import closing  # Importa closing para garantir que as conexões sejam fechadas corretamente

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path  # Inicializa o caminho do banco de dados

    def create_table_if_not_exists(self, table_name, schema):
        # Conecta ao banco de dados e cria a tabela se ela não existir
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(schema)  # Executa o esquema SQL para criar a tabela

    def load_data(self, data, table_name):
        # Carrega os dados em uma tabela no banco de dados
        with sqlite3.connect(self.db_path) as conn:
            data.to_sql(table_name, conn, if_exists='replace', index=False)  # Insere os dados na tabela, substituindo se já existir

