import pandas as pd
import requests
from ..sql_app.database_manager import DatabaseManager

class DataProcessor:
    def __init__(self, url, db_manager):
        self.url = url
        self.db_manager = db_manager

    def download_csv(self):
        response = requests.get(self.url)
        return response.content

    def process_csv(self, csv_content):
        # Criar um DataFrame do conteúdo CSV
        df = pd.read_csv(pd.compat.StringIO(csv_content.decode('utf-8')), delimiter=';')
        
        # Extrair colunas de anos diretamente das colunas do DataFrame
        year_columns = [col for col in df.columns if col.isdigit()]
        
        # Preparar dados para inserção no banco de dados
        data_to_insert = []
        for index, row in df.iterrows():
            for year in year_columns:
                data_to_insert.append((int(row['id']), row['produto'], row.get(year, 0), int(year)))
        return data_to_insert

    def run(self):
        self.db_manager.create_database()
        csv_content = self.download_csv()
        data_to_insert = self.process_csv(csv_content)
        self.db_manager.insert_data(data_to_insert)

if __name__ == '__main__':
    db_path = 'embrapa.db'
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    db_manager = DatabaseManager(db_path)
    processor = DataProcessor(url, db_manager)
    processor.run()

