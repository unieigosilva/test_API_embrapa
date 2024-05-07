import pandas as pd
import requests
from io import StringIO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CSVProcessor:
    def __init__(self, url, db_path):
        self.url = url
        self.db_path = db_path
        self.engine = create_engine(f'sqlite:///{self.db_path}')
        self.Session = sessionmaker(bind=self.engine)
        self.df = self.download_csv()

    def download_csv(self):
        """Baixa um arquivo CSV do URL especificado e retorna como um DataFrame."""
        response = requests.get(self.url)
        csv_raw = StringIO(response.text)
        df = pd.read_csv(csv_raw, delimiter=';')
        return df

    def add_total_row(self):
        """Adiciona uma linha 'Total' ao DataFrame para os produtos especificados."""
        categories = ["VINHO DE MESA", "VINHO FINO DE MESA (VINÍFERA)", "SUCO", "DERIVADOS"]
        df_filtered = self.df[self.df['produto'].isin(categories)]
        total = df_filtered.filter(regex='^\d{4}$').sum()
        total['produto'] = 'Total'
        total_df = pd.DataFrame([total], columns=self.df.columns)
        self.df = pd.concat([self.df, total_df], ignore_index=True)

    def insert_into_db(self):
        """Insere o DataFrame processado no banco de dados."""
        session = self.Session()
        try:
            self.df.to_sql('producao', self.engine, if_exists='append', index=False)
            session.commit()
            print("Dados inseridos com sucesso no banco de dados.")
        except Exception as e:
            print("Erro ao inserir dados no banco de dados:", e)
        finally:
            session.close()

def main():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    db_path = 'C:\Users\Igor\Desktop\Documentos\Pessoal\Pós-graduação\Project_pos\Faze_1_teste\scrape_api_project _2\app\sql_app\embrapa.db'  # Caminho correto conforme sua estrutura de pastas
    processor = CSVProcessor(url, db_path)
    processor.add_total_row()
    processor.insert_into_db()

if __name__ == "__main__":
    main()
