## Imports de bibliotecas padrão
from sqlalchemy.orm import Session
import logging

# Imports de bibliotecas padrão
from app.sql_app.database import get_db
from app.scrape.models import (
    ProductionData,
    ProcessingData,
    CommercializationData,
    ImportData,
    ExportData,
    ProcessingCategoriaEnum,
    ImportacaoCategoriaEnum,
    ExportacaoCategoriaEnum,
)
from app.utils.handlers import (
    get_production_data,
    get_processing_data,
    get_commercialization_data,
    get_import_data,
    get_export_data,
    get_production_bd,
    get_processing_data_bd,
    get_Commercialization_bd,
    get_read_importation_data_bd,
    get_exportation_data_bd,
    login_for_access_token,
    log_responses,
)

################################################################################################
################################################################################################
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm

################################################################################################
################################################################################################




app = FastAPI()

################################################################################################
################################################################################################

# Rota para login e geração de token
# Rota para login e geração de token
@app.post("/token")
async def token_route(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_for_access_token(form_data)


# Rota para login e geração de token


# Middleware para logar respostas de erro
@app.middleware("http")
async def login_route(request: Request, call_next):
    return await log_responses(request,call_next)

# Rota protegida para obter dados de produção
@app.get("/production/", response_model=ProductionData)
async def production_data_route(year: int, token: str):
    return await get_production_data(year, token)


# Rota protegida para obter dados de processamento
@app.get("/processing/", response_model=ProcessingData)
async def processing_data_route(category: ProcessingCategoriaEnum, year: int = None, token: str = None):
    return await get_processing_data(category, year, token)


@app.get("/commercialization/", response_model=CommercializationData)
async def commercialization_data_route(year: int, token: str):
    return await get_commercialization_data(year, token)


@app.get("/import/", response_model=ImportData)
async def import_data_route(category: ImportacaoCategoriaEnum, year: int = None, token: str =None):
     return await get_import_data(category, year, token)



@app.get("/export/", response_model=ExportData)
async def export_data_route(category: ExportacaoCategoriaEnum, year: int = None, token: str =None):
     return await get_export_data(category, year, token)


################################################################################################
################################################################################################
################################################################################################

 # Rota protegida para obter dados BD
@app.get("/bd/production/{year}")
async def read_production(year: int, db: Session = Depends(get_db), token: str = None):
    return await get_production_bd(year, db, token)

# Rota protegida para obter dados de processamento por categoria e ano
@app.get("/bd/processing/{category}/{year}")
async def read_processing_data(category: ProcessingCategoriaEnum, year: int, token: str = None):
    return await get_processing_data_bd(category, year, token)

@app.get("/bd/commercialization/{year}")
async def read_commercialization(year: int, db: Session = Depends(get_db), token: str = None):
    return await get_Commercialization_bd(year, db, token)


@app.get("/bd/importation/{category}/{year}")
async def read_importation_data_bd(category: ImportacaoCategoriaEnum, year: int, token: str = None):
    return await get_read_importation_data_bd(category, year, token)


@app.get("/bd/exportation/{category}/{year}")
async def read_exportation_data(category: ExportacaoCategoriaEnum, year: int, token: str = None):
    return await get_exportation_data_bd(category, year, token)