from datetime import datetime
from src.db.enums import OrderStatus
from src.db.tables.order import OrderBase


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    status: OrderStatus
