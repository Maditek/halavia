from sqlmodel import Session

from src.db.tables.toast import Toast


class ToastRepository:
    def __init__(self, session: Session) -> "ToastRepository":
        self.session = session

    def get(self, id: int):
        self.session.get(Toast, id)

    def create(self, toast: Toast) -> Toast:
        self.session.add(toast)
        self.session.commit()
        self.session.refresh(toast)
        return toast

    def delete(self, toast: Toast) -> None:
        self.session.delete(toast)
        self.session.commit()
