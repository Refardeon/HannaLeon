from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlmodel import Session
from starlette.middleware.cors import CORSMiddleware

from app.auth.utils import seed_users
from app.database import create_db_and_tables, get_session
from app.todo.router import router as todo_router
from app.auth.router import router as auth_router
from logging import getLogger, basicConfig, INFO

LOGGER = getLogger(__name__)
basicConfig(level=INFO)

LOGGER.info("Starting HannaLeonAPI")

@asynccontextmanager
async def lifespan(_app: FastAPI):
    LOGGER.info("Creating database and tables")
    create_db_and_tables()
    seed_users(next(get_session()))
    yield


app = FastAPI(title="HannaLeon", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://hanna-und-leon.de"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=auth_router)
app.include_router(router=todo_router)


@app.get("/")
async def root():
    return {"message": "HannaLeonAPI"}
