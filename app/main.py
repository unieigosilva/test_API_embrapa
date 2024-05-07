from fastapi import FastAPI, Request
import logging

from .scraper import (
    scrape_production,
    scrape_processing,
    scrape_commercialization,
    scrape_import,
    scrape_export,
)
from .models import (
    ProductionData,
    ProcessingData,
    CommercializationData,
    ImportData,
    ExportData,
)

# Configuração do Logger
logging.basicConfig(level=logging.ERROR, filename='error.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()

# Middleware para logar respostas de erro
@app.middleware("http")
async def log_responses(request: Request, call_next):
    response = await call_next(request)
    if response.status_code >= 400:
        logging.error(f"Erro HTTP: {response.status_code} para a URL {request.url}")
    return response

@app.get("/production/", response_model=ProductionData)
def get_production_data(year: int):
    try:
        # Tentativa de obter dados de processamento do site externo
        data = scrape_production(year)
    except Exception as e:
        # Log de erro se o scraping falhar
        logging.error(f"Falha ao buscar dados de produção para o ano {year}: {e}")
        # Retornando uma resposta de erro ao cliente da API
        return {"error": "Falha ao buscar dados de produção"}
        # Retorna os dados processados se não houver exceções
    return {"year": year, "data": data}

@app.get("/processing/", response_model=ProcessingData)
def get_processing_data(category: str, year: int = None):
    try:
        data = scrape_processing(category, year)
    except Exception as e:
        logging.error(f"Falha ao buscar dados de processamento para {category}, ano {year}: {e}")
        return {"error": "Falha ao buscar dados de processamento"}
    return {"category": category, "year": year, "data": data}

@app.get("/commercialization/", response_model=CommercializationData)
def get_commercialization_data(year: int):
    try:
        data = scrape_commercialization(year)
    except Exception as e:
        logging.error(f"Falha ao buscar dados de comercialização para o ano {year}: {e}")
        return {"error": "Falha ao buscar dados de comercialização"}
    return {"year": year, "data": data}

@app.get("/import/", response_model=ImportData)
def get_import_data(category: str, year: int = None):
    try:
        data = scrape_import(category, year)
    except Exception as e:
        logging.error(f"Falha ao buscar dados de importação para {category}, ano {year}: {e}")
        return {"error": "Falha ao buscar dados de importação"}
    return {"category": category, "year": year, "data": data}

@app.get("/export/", response_model=ExportData)
def get_export_data(category: str, year: int = None):
    try:
        data = scrape_export(category, year)
    except Exception as e:
        logging.error(f"Falha ao buscar dados de exportação para {category}, ano {year}: {e}")
        return {"error": "Falha ao buscar dados de exportação"}
    return {"category": category, "year": year, "data": data}