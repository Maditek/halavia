from datetime import datetime
from src.db.tables.user import UserBase


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
