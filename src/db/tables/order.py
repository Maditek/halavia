import datetime
from sqlmodel import Field, SQLModel

from src.db.enums import OrderStatus


class OrderBase(SQLModel):
    customer_name: str
    user_id: int = Field(foreign_key="users.id")


class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.datetime.now)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
