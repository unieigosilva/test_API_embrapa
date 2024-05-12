from pydantic import BaseModel,Field, validator
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel






class ProcessingCategoriaEnum(str, Enum):
    viniferas = "viniferas"
    americanas_hibridas = "americanas_hibridas"
    uvas_mesa = "uvas_mesa"
    sem_classificacao = "sem_classificacao"

class ImEXportacaoCategoriaEnum(str, Enum):
    vinhos_mesa = "vinhos_mesa"
    espumantes = "espumantes"
    uvas_frescas = "uvas_frescas"
    uvas_passas = "uvas_passas"
    suco_uva = "suco_uva"
    

class ProductDetail(BaseModel):
    Produto: str
    Quantidade: Optional[str] = Field(None, alias="Quantidade (L.)")

class ProductionData(BaseModel):
    year: int
    data: List[ProductDetail]


class ProcessingDetail(BaseModel):
    Cultivar: str
    Quantidade: Optional[str] = Field(None, alias="Quantidade (Kg)")

class ProcessingData(BaseModel):
    category: str
    year: Optional[int] = None
    data: List[ProcessingDetail]


class CommercializationDetail(BaseModel):
    Produto: str
    Quantidade: Optional[str] = Field(None, alias="Quantidade (L.)")


class CommercializationData(BaseModel):
    year: int
    data: List[ProductDetail]

class ImportDetail(BaseModel):
    Pais: Optional[str] = Field(None, alias="Países")
    Quantidade: Optional[str] = Field(None, alias="Quantidade (Kg)")
    Valor: Optional[str] = Field(None, alias="Valor (US$)")

class ImportData(BaseModel):
    year: Optional[int]
    data: List[ImportDetail]


class ExportDetail(BaseModel):
    Pais: Optional[str] = Field(None, alias="Países")
    Quantidade: Optional[str] = Field(None, alias="Quantidade (Kg)")
    Valor: Optional[str] = Field(None, alias="Valor (US$)")

class ExportData(BaseModel):
    year: Optional[int]
    data: List[ImportDetail]

class DateInput(BaseModel):
    year: int

class DateInput(BaseModel):
    year: int

    @validator('year')
    def check_year(cls, value):
        if 1970 <= value <= 2025:
            return value
        raise ValueError('Year must be between 1970 and 2025')