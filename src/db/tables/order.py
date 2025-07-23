import datetime
from sqlmodel import Field, SQLModel

from src.db.enums import OrderStatus


class OrderBase(SQLModel):
    user_id: int = Field(foreign_key="user.id")


class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
