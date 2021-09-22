from sqlmodel import SQLModel, create_engine, Session
from .fileops import get_config

config = get_config()
# sqlite_file_name = "/home/halum/.config/roamex/database.db"
sqlite_file_name = config["roamex_db_location"]

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
