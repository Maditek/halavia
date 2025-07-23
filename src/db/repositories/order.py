from sqlmodel import Session

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

    def update(self, order: Order) -> Order:
        self.session.add(order)
        self.session.commit(order)
        self.session.refresh(order)
        return order
