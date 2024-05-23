from app.data_processing.producao_processing import ProdDataCSV
from app.data_processing.processamento_processing import ProctDataCSV
from app.data_processing.comercializacao_processing import ComercDataCSV
from app.data_processing.importacao_processing import ImportDataCSV
from app.data_processing.exportacao_processing import ExportDataCSV
from app.config import Config_AC,settings_data_processing


import asyncio



    # Atualiza dados de produção
async def update_producacao():
    production_handler = ProdDataCSV()
    await  production_handler.download_csv()
    production_handler.setup_database()
    await  production_handler.load_into_database()
    await  production_handler.delete_csv_after_use()

async def update_processamento():
    # Configurações para cada tipo de Processa
    configurations = settings_data_processing['Processamento']['configurations']

    
    # Cria e executa o processo para cada configuração
    for config in configurations:
        csv_url = settings_data_processing['Processamento'][f'url_{config["key"]}']
        csv_path = settings_data_processing['Processamento'][f'CSV_{config["key"]}']
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

    configurations = settings_data_processing['Importacao']['configurations']

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

    configurations = settings_data_processing['Exportacao']['configurations']
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
    await asyncio.gather(
        update_producacao(),
        update_processamento(),
        update_comercializacao(),
        update_importacao(),
        update_exportacao()
    )

if __name__ == "__main__":
   
    
    import asyncio
    asyncio.run(update_database())