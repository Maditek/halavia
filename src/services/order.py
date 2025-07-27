from sqlmodel import Session

from src.api.scehmas.order import OrderCreate
from src.core.exceptions.order import OrderNotFoundException
from src.db.enums import OrderStatus
from src.db.repositories.order import OrderRepository
from src.db.tables.order import Order


class OrderService:
    def __init__(self, session: Session):
        self.repo = OrderRepository(session=session)

    def create_order(self, order_create: OrderCreate) -> Order:
        order = Order.model_validate(order_create)
        return self.repo.create(order=order)

    def get_by_id(self, id: int) -> Order:
        order = self.repo.get(id=id)
        if not order:
            raise OrderNotFoundException(id=id)
        return order

    def get_by_user_id(self, user_id: int) -> list[Order]:
        orders = self.repo.get_by_user_id(user_id=user_id)
        return orders

    def delete(self, order: Order) -> None:
        self.repo.delete(order=order)

    def update_status(self, order: Order, status: OrderStatus) -> Order:
        return self.repo.update_status(order=order, status=status)
