from enum import Enum


class OrderStatus(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    READY = "Ready"
    Delivered = "Delivered"


class BreadType(Enum):
    WHITE = "White"
    GLUTEN_FREE = "Gluten Free"
    WHOLE_WHEAT = "Whole Wheat"


class CutStyle(Enum):
    TRIANGLES = "Triangles"
    SQUARES = "Squares"
    NONE = "None"
