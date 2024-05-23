import pandas as pd
import requests
from app.sql_app.database_manager import DatabaseManager
from app.config import settings_data_processing
import os

class ProctDataCSV:
    def __init__(self, csv_url, csv_path, table_name):
        self.csv_url = csv_url
        self.csv_path = csv_path
        self.table_name = table_name
        database_path = settings_data_processing['database_path']  
        self.db_manager = DatabaseManager(database_path)

    async def download_csv(self):
        response = requests.get(self.csv_url)
        with open(self.csv_path, 'wb') as f:
            f.write(response.content)
        print("Arquivo baixado com sucesso.")

    async def process_csv(self):
        data = pd.read_csv(self.csv_path, delimiter='\t')
        data.drop(columns=data.columns[1], inplace=True)
        return data


    async def load_into_database(self):
        data = await self.process_csv()
        self.db_manager.load_data(data, self.table_name)
        print(f"Dados carregados no banco de dados para a tabela {self.table_name} com sucesso.")

    async def delete_csv_after_use(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
            print("Arquivo CSV removido após o uso.")

    def setup_database(self):
        schema = f"CREATE TABLE IF NOT EXISTS {self.table_name} (produto TEXT, quantidade REAL)"
        self.db_manager.create_table_if_not_exists(self.table_name, schema)
