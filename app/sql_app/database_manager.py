import sqlite3
from contextlib import closing

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_table_if_not_exists(self, table_name, schema):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(schema)

    def load_data(self, data, table_name):
        with sqlite3.connect(self.db_path) as conn:
            data.to_sql(table_name, conn, if_exists='replace', index=False)

"""
def load_data(self, data, table_name):
    with sqlite3.connect(self.db_path) as conn:
        data.to_sql(table_name, conn, if_exists='append', index=False)
Alternativa para Sobreposição Sem Perda de Dados:
Se você deseja adicionar novos dados aos existentes sem excluir os dados antigos, você poderia usar if_exists='append'. 
Com append, os dados do DataFrame são adicionados ao final da tabela existente sem alterar ou deletar os dados que já estavam lá.
"""
