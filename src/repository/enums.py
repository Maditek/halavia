from enum import Enum


class OrderStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In_Progress"
    READY = "Ready"
    Delivered = "Delivered"
