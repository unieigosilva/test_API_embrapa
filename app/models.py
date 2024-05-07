from pydantic import BaseModel,Field
from typing import List, Optional



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

