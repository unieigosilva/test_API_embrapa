DATABASE_PATH = "./app/sql_app/embrapa.db"
BASE_URL = "http://vitibrasil.cnpuv.embrapa.br/index.php"



PROCESSING_CATEGORIES = [
    "viniferas",
    "americanas_hibridas",
    "uvas_mesa",
    "sem_classificacao"
]

settings_data_processing = {
    "database_path": DATABASE_PATH,
    "producao": {
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "CSV": "Producao.csv"
    },
    "Processamento": {
        "url_01": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaViniferas.csv",
        "url_02": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaAmericanas.csv",
        "url_03": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaMesa.csv",
        "url_04": "http://vitibrasil.cnpuv.embrapa.br/download/ProcessaSemclass.csv",
        "CSV_01": "ProcessaViniferas.csv",
        "CSV_02": "ProcessaAmericanas.csv",
        "CSV_03": "ProcessaMesa.csv",
        "CSV_04": "ProcessaSemclass.csv",
        "configurations": [
            {'key': '01', 'table_suffix': 'viniferas'},
            {'key': '02', 'table_suffix': 'americanas_hibridas'},
            {'key': '03', 'table_suffix': 'uvas_mesa'},
            {'key': '04', 'table_suffix': 'sem_classificacao'}
        ]
    },
    "Comercializacao": {
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv",
        "CSV": "Comercio.csv"
    },
    "Importacao": {
        "url_01": "http://vitibrasil.cnpuv.embrapa.br/download/ImpVinhos.csv",
        "url_02": "http://vitibrasil.cnpuv.embrapa.br/download/ImpEspumantes.csv",
        "url_03": "http://vitibrasil.cnpuv.embrapa.br/download/ImpFrescas.csv",
        "url_04": "http://vitibrasil.cnpuv.embrapa.br/download/ImpPassas.csv",
        "url_05": "http://vitibrasil.cnpuv.embrapa.br/download/ImpSuco.csv",
        "CSV_01": "ImpVinhos.csv",
        "CSV_02": "ImpEspumantes.csv",
        "CSV_03": "ImpFrescas.csv",
        "CSV_04": "ImpPassas.csv",
        "CSV_05": "ImpSuco.csv",
        "configurations": [
            {'key': '01', 'table_suffix': 'vinhos_mesa'},
            {'key': '02', 'table_suffix': 'espumantes'},
            {'key': '03', 'table_suffix': 'uvas_frescas'},
            {'key': '04', 'table_suffix': 'uvas_passas'},
            {'key': '05', 'table_suffix': 'suco_uva'}
        ]
    },
    "Exportacao": {
        "url_01": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "url_02": "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "url_03": "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "url_04": "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "CSV_01": "ExpVinho.csv",
        "CSV_02": "ExpEspumantes.csv",
        "CSV_03": "ExpUva.csv",
        "CSV_04": "ExpSuco.csv",
        "configurations": [
            {'key': '01', 'table_suffix': 'vinhos_mesa'},
            {'key': '02', 'table_suffix': 'espumantes'},
            {'key': '03', 'table_suffix': 'uvas_frescas'},
            {'key': '04', 'table_suffix': 'suco_uva'}
        ]
    },
}

scraper = {
    "base_url": BASE_URL,
    "processing": {
        "viniferas": "subopt_01",
        "americanas_hibridas": "subopt_02",
        "uvas_mesa": "subopt_03",
        "sem_classificacao": "subopt_04",
    },
    "import": {
        "vinhos_mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas_frescas": "subopt_03",
        "uvas_passas": "subopt_04",
        "suco_uva": "subopt_05",
    },
    "export": {
        "vinhos_mesa": "subopt_01",
        "espumantes": "subopt_02",
        "uvas_frescas": "subopt_03",
        "suco_uva": "subopt_04",
    }
}

sql_app = {
    "database_path": DATABASE_PATH,
    "processing": {
        "viniferas": "Processamento_viniferas",
        "americanas_hibridas": "Processamento_americanas_hibridas",
        "uvas_mesa": "Processamento_uvas_mesa",
        "sem_classificacao": "Processamento_sem_classificacao"
    },
    "import": {
        "vinhos_mesa": "Importacao_vinhos_mesa",
        "espumantes": "Importacao_espumantes",
        "uvas_frescas": "Importacao_uvas_frescas",
        "uvas_passas": "Importacao_uvas_passas",
        "suco_uva": "Importacao_suco_uva"
    },
    "export": {
        "vinhos_mesa": "Exportacao_vinhos_mesa",
        "espumantes": "Exportacao_espumantes",
        "uvas_frescas": "Exportacao_uvas_frescas",
        "suco_uva": "Exportacao_suco_uva"
    }
}


class Config_AC:
    @staticmethod
    def get(setting_name, key=None):
        if key:
            return settings_data_processing.get(setting_name, {}).get(key, None)
        else:
            # Retorna o valor diretamente se nenhum sub-chave é especificada
            return settings_data_processing.get(setting_name, None)

