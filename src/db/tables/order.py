from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from src.db.enums import BreadType, CutStyle, OrderStatus


class OrderBase(SQLModel):
    user_id: int = Field(foreign_key="user.id")
    bread_type: BreadType = Field(default=BreadType.WHITE)
    cut_style: CutStyle = Field(default=CutStyle.TRIANGLES)


class Order(OrderBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
