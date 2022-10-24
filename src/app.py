import uvicorn
from fastapi import FastAPI, Request
import time

from database.database import Base, engine
from routers import home, items, token

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


app.include_router(home.router)
app.include_router(items.router)
app.include_router(token.router)



if __name__ == "__main__":
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)
