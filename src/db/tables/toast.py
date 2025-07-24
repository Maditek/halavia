from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

from src.db.enums import BreadType, CutStyle

if TYPE_CHECKING:
    from src.db.tables.order import Order


class ToastBase(SQLModel):
    order_id: int = Field(foreign_key="order.id")
    bread_type: BreadType = Field(default=BreadType.WHITE)
    cut_style: CutStyle = Field(default=CutStyle.TRIANGLES)


class Toast(ToastBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    order: Order = Relationship(back_populates="toasts")
