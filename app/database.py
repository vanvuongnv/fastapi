
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from settings import SQLALCHEMY_DATABASE_URL


def get_db_context():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

metadata = MetaData().create_all(engine)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()