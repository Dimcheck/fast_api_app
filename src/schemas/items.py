from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Optional, Union

from pydantic import BaseModel, Field, ValidationError, validator


class ItemSchema(BaseModel):
    id: Decimal
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    is_broken: bool

    class Config:
        orm_mode = True


class CryptoSchema(BaseModel):
    asset_name: str = Field(default='BTCUSDT', alias='ticker')
    signal: int = Field(default=-1)
    close: Decimal = Field(default=20001.12)
    open: Decimal = Field(default=19153.12)
    high: Decimal = Field(default=20010.12)
    low: Decimal = Field(default=19953.12)
    time: datetime = Field(default=datetime.now())
    timenow: datetime = Field(default=datetime.now())
    interval: int = Field(default=5)
    plot_0: Optional[Decimal]
    plot_1: Optional[Decimal]

    # @validator(*[f"plot_{i}" for i in range(20)], pre=True)
    @validator('plot_0', 'plot_1', pre=True)
    def check_null(cls, v):
        if v == 'NULL':
            v = None
        return v

    class Config:
        orm_mode = True
