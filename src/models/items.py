from database.database import Base
from sqlalchemy import Boolean, Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=30), index=True)
    description = Column(String(length=100))
    price = Column(Float, index=True)
    is_broken = Column(Boolean, default=False)
