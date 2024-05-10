import pandas as pd
import requests
from app.sql_app.database_manager import DatabaseManager
from app.config import Config_AC

class ProcesDataCSV:
    def __init__(self):
        self.csv_url = Config_AC.get('producao', 'url')
        self.csv_path = Config_AC.get('producao', 'CSV')
        self.db_manager = DatabaseManager('C:/Users/Igor/Desktop/Projetos_python/pos_graduacao/Fase_1/test_API_embrapa/app/sql_app/embrapa.db')

    def download_csv(self):
        response = requests.get(self.csv_url)
        with open(self.csv_path, 'wb') as f:
            f.write(response.content)
        print("Arquivo baixado com sucesso.")

    def process_csv(self):
        data = pd.read_csv(self.csv_path, delimiter=';')
        data.drop(columns=data.columns[1], inplace=True)
        return data

    def load_into_database(self):
        data = self.process_csv()
        self.db_manager.load_data(data, 'producao')
        print("Dados carregados no banco de dados com sucesso.")

    def delete_csv_after_use(self):
        import os
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
            print("Arquivo CSV removido após o uso.")

    def setup_database(self):
        schema = "CREATE TABLE IF NOT EXISTS producao (produto TEXT, quantidade REAL)"
        self.db_manager.create_table_if_not_exists("producao", schema)

if __name__ == "__main__":
    handler = ProcesDataCSV()
    handler.download_csv()
    handler.setup_database()
    handler.load_into_database()
    handler.delete_csv_after_use()
