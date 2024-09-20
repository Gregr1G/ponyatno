from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from starlette.middleware.cors import CORSMiddleware

from src.routers import *
from src.Auth.invates.models import *
from src.Post.models import *
from database import create_db_and_tables, User



origins = [
    "http://localhost",
    "http://localhost:8080",
]



app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(get_apps_router())



if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True)