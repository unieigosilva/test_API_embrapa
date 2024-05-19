# Adicionar o diretório raiz do projeto ao sys.path
import sys
sys.path.append('./app/')


from data_processing.producao_processing import ProdDataCSV
from data_processing.processamento_processing import ProctDataCSV
from data_processing.comercializacao_processing import ComercDataCSV
from data_processing.importacao_processing import ImportDataCSV
from data_processing.exportacao_processing import ExportDataCSV
from config import Config_AC


    # Atualiza dados de produção
async def update_producacao():
    production_handler = ProdDataCSV()
    await  production_handler.download_csv()
    production_handler.setup_database()
    await  production_handler.load_into_database()
    await  production_handler.delete_csv_after_use()

async def update_processamento():
    # Configurações para cada tipo de Processa
    configurations = [
        {'key': '01', 'table_suffix': 'viniferas'},
        {'key': '02', 'table_suffix': 'americanas_hibridas'},
        {'key': '03', 'table_suffix': 'uvas_mesa'},
        {'key': '04', 'table_suffix': 'sem_classificacao'}
    ]

    # Cria e executa o processo para cada configuração
    for config in configurations:
        csv_url = Config_AC.get('Processamento', f'url_{config["key"]}')
        csv_path = Config_AC.get('Processamento', f'CSV_{config["key"]}')
        table_name = f'Processamento_{config["table_suffix"]}'
        handler = ProctDataCSV(csv_url, csv_path, table_name)
        await handler.download_csv()
        handler.setup_database()
        await handler.load_into_database()
        await handler.delete_csv_after_use()


async def update_comercializacao():
    # Instancia a classe e executa os métodos
    comerc_handler = ComercDataCSV()
    await comerc_handler.download_csv()
    comerc_handler.setup_database()
    await comerc_handler.load_into_database()
    await comerc_handler.delete_csv_after_use()


async def update_importacao():

    configurations = [
        {'key': '01', 'table_suffix': 'vinhos_mesa'},
        {'key': '02', 'table_suffix': 'espumantes'},
        {'key': '03', 'table_suffix': 'uvas_frescas'},
        {'key': '04', 'table_suffix': 'uvas_passas'},
        {'key': '05', 'table_suffix': 'suco_uva'}
    ]

    # Cria e executa o processo para cada configuração.
    for config in configurations:
        csv_url = Config_AC.get('Importacao', f'url_{config["key"]}')
        csv_path = Config_AC.get('Importacao', f'CSV_{config["key"]}')
        table_name = f'Importacao_{config["table_suffix"]}'
        
        handler = ImportDataCSV(csv_url, csv_path, table_name)
        await handler.download_csv()
        handler.setup_database()
        await handler.load_into_database()
        await  handler.delete_csv_after_use()

async def update_exportacao():

    configurations = [
        {'key': '01', 'table_suffix': 'vinhos_mesa'},
        {'key': '02', 'table_suffix': 'espumantes'},
        {'key': '03', 'table_suffix': 'uvas_frescas'},
        {'key': '04', 'table_suffix': 'suco_uva'}
    ]
    # Cria e executa o processo para cada configuração.
    for config in configurations:
        csv_url = Config_AC.get('Exportacao', f'url_{config["key"]}')
        csv_path = Config_AC.get('Exportacao', f'CSV_{config["key"]}')
        table_name = f'Exportacao_{config["table_suffix"]}'
        handler = ExportDataCSV(csv_url, csv_path, table_name)
        await  handler.download_csv()
        handler.setup_database()
        await  handler.load_into_database()
        await  handler.delete_csv_after_use()

async def update_database():
    await update_producacao()
    await update_processamento()
    await update_comercializacao()
    await update_importacao()
    await update_exportacao()

if __name__ == "__main__":
   
    
    import asyncio
    asyncio.run(update_database())