from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db.init.db import create_db_and_tables
from db.tables import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()


app = FastAPI(lifespan=lifespan)
