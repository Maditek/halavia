class OrderException(Exception):
    def __init__(self, message: str):
        self.message = message


class OrderNotFoundException(OrderException):
    def __init__(self, id: int):
        super().__init__(message=f"Order {id} not found")
