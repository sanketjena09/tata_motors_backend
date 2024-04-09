from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_user = "root"
_password = "root"
_db = "monalisha_motors"
_host = "localhost"
_port = "3306"

DB_URL = f"mysql+pymysql://{_user}:{_password}@{_host}:{_port}/{_db}"

_engine = create_engine(DB_URL)

Session = sessionmaker(bind=_engine)