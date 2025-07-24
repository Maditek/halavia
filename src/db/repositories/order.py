from sqlmodel import Session, select

from src.db.enums import OrderStatus
from src.db.tables.order import Order


class OrderRepository:
    def __init__(self, session: Session) -> "OrderRepository":
        self.session = session

    def get(self, id: int) -> Order:
        return self.session.get(Order, id)

    def create(self, order: Order) -> Order:
        self.session.add(order)
        self.session.commit(order)
        self.session.refresh(order)
        return order

    def update_status(self, order: Order, status: OrderStatus) -> Order:
        order.status = status
        self.session.add(order)
        self.session.commit(order)
        self.session.refresh(order)
        return order

    def delete(self, order: Order) -> None:
        self.session.delete(order)
        self.session.commit()

    def get_by_user_id(self, user_id: int) -> list[Order]:
        statement = select(Order).where(Order.user_id == user_id)
        orders = self.session.exec(statement).all()
        return orders
