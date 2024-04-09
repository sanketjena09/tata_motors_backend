from .db import Session
from typing import Generator

def get_db() -> Generator:
    try:
        session = Session()
        yield session
    finally:
        session.close()