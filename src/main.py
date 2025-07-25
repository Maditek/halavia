from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.core.exceptions.order import OrderNotFoundException
from src.db.init.db import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.exception_handler(OrderNotFoundException)
def order_not_found_handler(request: Request, exc: OrderNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            f"error": f"{exc.message}",
        },
    )
