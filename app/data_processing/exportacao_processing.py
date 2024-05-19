# Adicionar o diretório raiz do projeto ao sys.path
import sys
sys.path.append('./app/')

import pandas as pd
import requests
from sql_app.database_manager import DatabaseManager
from config import Config_AC
import os

class ExportDataCSV:
    def __init__(self, csv_url, csv_path, table_name):
        self.csv_url = csv_url
        self.csv_path = csv_path
        self.table_name = table_name
        database_path = Config_AC.get('database_path')  
        self.db_manager = DatabaseManager(database_path)
        print(database_path)
    def download_csv(self):
        response = requests.get(self.csv_url)
        with open(self.csv_path, 'wb') as f:
            f.write(response.content)
        print("Arquivo baixado com sucesso.")

    def process_csv(self):
        data = pd.read_csv(self.csv_path, delimiter=';')
        #data.drop(columns=data.columns[1], inplace=True)
        return data


    def load_into_database(self):
        data = self.process_csv()
        self.db_manager.load_data(data, self.table_name)
        print(f"Dados carregados no banco de dados para a tabela {self.table_name} com sucesso.")

    def delete_csv_after_use(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)
            print("Arquivo CSV removido após o uso.")

    def setup_database(self):
        schema = f"CREATE TABLE IF NOT EXISTS {self.table_name} (produto TEXT, quantidade REAL)"
        self.db_manager.create_table_if_not_exists(self.table_name, schema)

if __name__ == "__main__":
    # Configurações para cada tipo de ExportDataCSV.
    #table_suffix: table_suffix é um sufixo (ou parte final) que é adicionado ao nome base da tabela para formar o nome completo da tabela
    configurations = [
        {'key': '01', 'table_suffix': 'vinhos_mesa'},
        {'key': '02', 'table_suffix': 'espumantes'},
        {'key': '03', 'table_suffix': 'uvas_frescas'},
        {'key': '04', 'table_suffix': 'suco_uva'},
    ]

    # Cria e executa o processo para cada configuração.
    for config in configurations:
        csv_url = Config_AC.get('Exportacao', f'url_{config["key"]}')
        csv_path = Config_AC.get('Exportacao', f'CSV_{config["key"]}')
        table_name = f'Exportacao_{config["table_suffix"]}'
        
        handler = ExportDataCSV(csv_url, csv_path, table_name)
        handler.download_csv()
        handler.setup_database()
        handler.load_into_database()
        handler.delete_csv_after_use()
