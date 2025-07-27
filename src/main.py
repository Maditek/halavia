from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.core.exceptions.order import OrderNotFoundException
from src.core.exceptions.user import (
    UserAlreadyExistsException,
    UserIdNotFoundException,
    UserNameNotFoundException,
)
from src.db.init.db import create_db_and_tables
from src.api.routes import order_router, user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan, title="Halavia")


@app.exception_handler(OrderNotFoundException)
def order_not_found_handler(request: Request, exc: OrderNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            f"error": f"{exc.message}",
        },
    )


@app.exception_handler(UserIdNotFoundException)
def order_not_found_handler(request: Request, exc: UserIdNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            f"error": f"{exc.message}",
        },
    )


@app.exception_handler(UserNameNotFoundException)
def order_not_found_handler(request: Request, exc: UserNameNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            f"error": f"{exc.message}",
        },
    )


@app.exception_handler(UserAlreadyExistsException)
def order_not_found_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(
        status_code=409,
        content={
            f"error": f"{exc.message}",
        },
    )


app.include_router(order_router)
app.include_router(user_router)
