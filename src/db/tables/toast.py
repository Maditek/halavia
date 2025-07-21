from sqlmodel import Field, SQLModel

from src.db.enums import BreadType, CutStyle


class ToastBase(SQLModel):
    order_id: int = Field(foreign_key="order.id")
    bread_type: BreadType = Field(default=BreadType.WHITE)
    cut_style: CutStyle = Field(default=CutStyle.TRIANGLES)


class Toast(ToastBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
