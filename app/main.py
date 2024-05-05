from fastapi import FastAPI
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

app = FastAPI()

@app.get("/production/", response_model=ProductionData)
def get_production_data(year: int):
    data = scrape_production(year)
    return {"year": year, "data": data}

@app.get("/processing/", response_model=ProcessingData)
def get_processing_data(category: str, year: int = None):
    data = scrape_processing(category, year)
    return {"category": category, "year": year, "data": data}

@app.get("/commercialization/", response_model=CommercializationData)
def get_commercialization_data(year: int):
    data = scrape_commercialization(year)
    return {"year": year, "data": data}

@app.get("/import/", response_model=ImportData)
def get_import_data(category: str, year: int = None):
    data = scrape_import(category, year)
    return {"category": category, "year": year, "data": data}

@app.get("/export/", response_model=ExportData)
def get_export_data(category: str, year: int = None):
    data = scrape_export(category, year)
    return {"category": category, "year": year, "data": data}