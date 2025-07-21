import datetime
from sqlmodel import Field, SQLModel, table


class UserBase(SQLModel):
    name: str = Field(unique=True)


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.datetime.now)
