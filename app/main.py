from fastapi import FastAPI, Request
import logging

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.sql_app.database import get_db
from app.sql_app.models import (
    Production, 
    Commercialization,
    Processing,
    Importation,
    Exportation,

)

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
    ProcessingCategoriaEnum,
    ImEXportacaoCategoriaEnum,
)

################################################################################################
################################################################################################
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
import logging

################################################################################################
################################################################################################

# Configuração do Logger
logging.basicConfig(level=logging.ERROR, filename='error.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()



################################################################################################
################################################################################################



# Configuração do Logger
logging.basicConfig(level=logging.ERROR, filename='error.log', format='%(asctime)s - %(levelname)s - %(message)s')

# Definições de segurança JWT
SECRET_KEY = "sua_chave_secreta_123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Esquema de autenticação OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

#######################################################################
#######################################################################
# Simulação de banco de dados de usuários
fake_users_db = {
    "teste": {
        "username": "teste",
        "hashed_password": "fakehashedteste"
    }
}

# Função para 'hash' de senha simulada
def fake_hash_password(password: str):
    return "fakehashed" + password

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or "fakehashed" + password != user["hashed_password"]:
        return False
    return user
######################################################################
#####################################################################

# Geração do token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Rota para login e geração de token
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais incorretas")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Função para verificar o token JWT
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in fake_users_db:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return fake_users_db[username]
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

################################################################################################
################################################################################################
################################################################################################
################################################################################################
# Middleware para logar respostas de erro
@app.middleware("http")
async def log_responses(request: Request, call_next):
    response = await call_next(request)
    if response.status_code >= 400:
        logging.error(f"Erro HTTP: {response.status_code} para a URL {request.url}")
    return response

# Rota protegida para obter dados de produção
@app.get("/production/", response_model=ProductionData)
async def get_production_data(year: int, token: str):
    user = verify_token(token)
    try:
        data = scrape_production(year)  
        return {"year": year, "data": data}
    except Exception as e:
        logging.error(f"Falha ao buscar dados de produção para o ano {year}: {e}")
        raise HTTPException(status_code=500, detail=f"Falha ao buscar dados de produção: {e}")


@app.get("/processing/", response_model=ProcessingData)
async def get_processing_data(category: ProcessingCategoriaEnum, year: int = None, token: str =None):
    user = verify_token(token)
    try:
        data = scrape_processing(category, year)
        return {"category": category, "year": year, "data": data}
    except Exception as e:
        logging.error(f"Falha ao buscar dados de processamento para {category}, ano {year}: {e}")
    raise HTTPException(status_code=500, detail=f"Falha ao buscar dados de processamento: {e}")


@app.get("/commercialization/", response_model=CommercializationData)
async def get_commercialization_data(year: int, token: str):
    user = verify_token(token)
    try:
        data = scrape_commercialization(year)
        return {"year": year, "data": data}
    except Exception as e:
        logging.error(f"Falha ao buscar dados de comercialização para o ano {year}: {e}")
        raise HTTPException(status_code=500, detail=f"Falha ao buscar dados de comercialização: {e}")
    

@app.get("/import/", response_model=ImportData)
async def get_import_data(category: ImEXportacaoCategoriaEnum, year: int = None, token: str =None):
    user = verify_token(token)
    try:
        data = scrape_import(category, year)
        return {"category": category, "year": year, "data": data}
    except Exception as e:
        logging.error(f"Falha ao buscar dados de importação para {category}, ano {year}: {e}")
    raise HTTPException(status_code=500, detail=f"Falha ao buscar dados de importação: {e}")

@app.get("/export/", response_model=ExportData)
async def get_export_data(category: ImEXportacaoCategoriaEnum, year: int = None, token: str =None):
    user = verify_token(token)
    try:
        data = scrape_export(category, year)
        return {"category": category, "year": year, "data": data}
    except Exception as e:
        logging.error(f"Falha ao buscar dados de exportação para {category}, ano {year}: {e}")
    raise HTTPException(status_code=500, detail=f"Falha ao buscar dados de exportação: {e}")

################################################################################################
################################################################################################
################################################################################################

@app.get("/bd/production/{year}")
async def read_production(year: int, db: Session = Depends(get_db), token: str = None):
    user = verify_token(token)
    try:
        data = Production.get_production_by_year(year)
        return {"year": year, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logging.error(f"Falha ao buscar dados de produção para o ano {year}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/bd/processing/{category}/{year}")
async def read_processing_data(category: ProcessingCategoriaEnum, year: int, token: str = None):
    user = verify_token(token)
    try:
        data = Processing.get_data_by_category_and_year(category, year)
        return {"category": category, "year": year, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logging.error(f"Falha ao buscar dados de processamento para {category}, ano {year}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/bd/commercialization/{year}")
async def read_commercialization(year: int, db: Session = Depends(get_db), token: str = None):
    user = verify_token(token)
    try:
        data = Commercialization.get_commercialization_by_year(year)
        return {"year": year, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logging.error(f"Falha ao buscar dados de comercialização para o ano {year}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/bd/importation/{category}/{year}")
async def read_importation_data(category: ImEXportacaoCategoriaEnum, year: int, token: str = None):
    user = verify_token(token)
    try:
        data = Importation.get_data_by_category_and_year(category, year)
        return {"category": category, "year": year, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logging.error(f"Falha ao buscar dados de importação para {category}, ano {year}: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/bd/exportation/{category}/{year}")
async def read_exportation_data(category: ImEXportacaoCategoriaEnum, year: int, token: str = None):
    user = verify_token(token)
    try:
        data = Exportation.get_data_by_category_and_year(category, year)
        return {"category": category, "year": year, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logging.error(f"Falha ao buscar dados de exportação para {category}, ano {year}: {e}")
        raise HTTPException(status_code=500, detail=str(e))