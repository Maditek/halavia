import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from src.db.enums import OrderStatus

if TYPE_CHECKING:
    from src.db.tables.toast import Toast


class OrderBase(SQLModel):
    user_id: int = Field(foreign_key="user.id")


class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    status: OrderStatus = Field(default=OrderStatus.PENDING)

    toasts: list["Toast"] = Relationship(back_populates="order", cascade_delete=True)
