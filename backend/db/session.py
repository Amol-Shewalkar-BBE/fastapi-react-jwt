from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

# define database url
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# start database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# start the session
SESSIONLOCAL = sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db() -> Generator:
    db = SESSIONLOCAL()
    try:
        yield db
    finally:
        db.close()

        