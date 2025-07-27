from sqlmodel import Session

from src.api.scehmas.user import UserCreate
from src.core.exceptions.user import (
    UserAlreadyExistsException,
    UserIdNotFoundException,
    UserNameNotFoundException,
)
from src.db.repositories.user import UserRepository
from src.db.tables.user import User


class UserService:
    def __init__(self, session: Session) -> "UserService":
        self.repo = UserRepository(session=session)

    def get_by_id(self, id: int) -> User:
        user = self.repo.get_by_id(id=id)
        if not user:
            raise UserIdNotFoundException(id=id)
        return user

    def get_by_name(self, name: str) -> User:
        user = self.repo.get_by_name(name=name)
        if not user:
            raise UserNameNotFoundException(name=name)
        return user

    def create(self, user_create: UserCreate) -> User:
        user = User.model_validate(user_create)
        print(user.name)
        if self.repo.get_by_name(user.name):
            raise UserAlreadyExistsException(name=user.name)
        return self.repo.create(user)

    def delete(self, user: User) -> None:
        self.repo.delete(user)
