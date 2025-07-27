from fastapi import APIRouter, Depends
from sqlmodel import Session

from src.api.scehmas.order import OrderCreate, OrderResponse
from src.db.session import get_session
from src.services.order import OrderService


router = APIRouter(prefix="/order")


def get_order_service(session: Session = Depends(get_session)) -> OrderService:
    return OrderService(session)


@router.get("/", response_model=OrderResponse)
async def get_order(id: int, service: OrderService = Depends(get_order_service)):
    return service.get_by_id(id=id)


@router.post("/", response_model=OrderResponse)
async def create_order(
    order: OrderCreate, service: OrderService = Depends(get_order_service)
):
    return service.create_order(order_create=order)
