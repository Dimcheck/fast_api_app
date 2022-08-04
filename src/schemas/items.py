from typing import Optional
from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    is_broken: bool

    class Config:
        orm_mode = True
