from sqlmodel import Field, SQLModel, create_engine, Relationship
from typing import Optional
from datetime import date
from decimal import Decimal

class Subscrition(SQLModel, table=True):
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal

class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key='subscrition.id')
    subscription: Subscrition = Relationship()
    date: date


