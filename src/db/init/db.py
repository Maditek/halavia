from sqlmodel import SQLModel, create_engine
from src.db.tables import *
from src.core.settings import get_settings


db_url = get_settings().db_url
print(db_url)
engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
