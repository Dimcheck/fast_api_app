from fastapi import FastAPI

from routers import home, items
from database.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(home.router)
app.include_router(items.router)
