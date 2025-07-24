from sqlmodel import Session, select

from src.db.tables.user import User


class UserRepository:
    def __init__(self, session: Session) -> "UserRepository":
        self.session = session

    def get_by_id(self, id: int) -> User:
        return self.session.get(User, id)

    def get_by_name(self, name: str) -> User:
        statement = select(User).where(User.name == name)
        return self.session.exec(statement).first()

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def delete(self, user: User) -> None:
        self.session.delete(user)
        self.session.commit()
