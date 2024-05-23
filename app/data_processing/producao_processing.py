import pandas as pd
import requests
from app.sql_app.database_manager import DatabaseManager
from app.config import settings_data_processing
import os


class ProdDataCSV:
    def __init__(self):
        self.csv_url = settings_data_processing['producao']['url']
        self.csv_path = settings_data_processing['producao']['CSV']
        database_path = settings_data_processing['database_path'] 
        self.db_manager = DatabaseManager(database_path)

    def setup_database(self):
        schema = "CREATE TABLE IF NOT EXISTS producao (produto TEXT, quantidade REAL)"
        self.db_manager.create_table_if_not_exists("producao", schema)

    async def download_csv(self):
        response = requests.get(self.csv_url)
        with open(self.csv_path, 'wb') as f:
            f.write(response.content)
        print("Arquivo baixado com sucesso.")

    async def process_csv(self):
        data = pd.read_csv(self.csv_path, delimiter=';')
        data.drop(columns=data.columns[1], inplace=True)
        return data

    async  def load_into_database(self):
        data = await self.process_csv()
        self.db_manager.load_data(data, 'producao')
        print("Dados carregados no banco de dados com sucesso.")

    async  def delete_csv_after_use(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
            print("Arquivo CSV removido após o uso.")



