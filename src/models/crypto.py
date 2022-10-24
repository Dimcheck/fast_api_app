from database.database import Base
from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.orm import relationship


class Crypto(Base):
    __tablename__ = 'crypto'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    asset_name = Column(String(length=30), index=True)
    signal = Column(Integer, index=True)
    close = Column(Numeric, index=True)
    open = Column(Numeric, index=True)
    high = Column(Numeric, index=True)
    low = Column(Numeric, index=True)
    time = Column(DateTime, index=True)
    timenow = Column(DateTime, index=True)
    interval = Column(Integer, index=True)
    plot_0 = Column(Numeric, index=True)
    plot_1 = Column(Numeric, index=True)

    class Config:
        orm_mode = True
