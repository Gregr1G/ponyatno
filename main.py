from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn

from src.routers import *
from src.Auth.invates.models import *
from database import create_db_and_tables, User



@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(get_apps_router())



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)