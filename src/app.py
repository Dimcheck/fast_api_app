import uvicorn
from fastapi import FastAPI

from database.database import Base, engine
from routers import home, items, token

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(home.router)
app.include_router(items.router)
app.include_router(token.router)

if __name__ == "__main__":
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)
