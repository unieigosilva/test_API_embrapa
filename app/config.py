settings_data_processing = {
    "producao": {
        "url": "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv",
        "CSV": "Producao.csv"
    },
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
        "CSV_04": "ProcessaSemclass.csv"
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
        "CSV_05": "ImpSuco.csv"
    },
    "Exportacao": {
        "url_01": "http://vitibrasil.cnpuv.embrapa.br/download/ExpVinho.csv",
        "url_02": "http://vitibrasil.cnpuv.embrapa.br/download/ExpEspumantes.csv",
        "url_03": "http://vitibrasil.cnpuv.embrapa.br/download/ExpUva.csv",
        "url_04": "http://vitibrasil.cnpuv.embrapa.br/download/ExpSuco.csv",
        "CSV_01": "ExpVinho.csv",
        "CSV_02": "ExpEspumantes.csv",
        "CSV_03": "ExpUva.csv",
        "CSV_04": "ExpSuco.csv"
    },
}


class Config_AC:
    @staticmethod
    def get(setting_name, key):
        return settings_data_processing.get(setting_name, {}).get(key, None)
    

