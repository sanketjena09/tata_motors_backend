from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_user = "monalisha_motors_user"
_password = "ZJCP3MqtH84r2hSAATbGItk4o4eSe3Un"
_db = "monalisha_motors"
_host = "dpg-coivkmdjm4es739vefig-a.oregon-postgres.render.com"
_port = "5432"


DB_URL = f"postgresql+psycopg2://{_user}:{_password}@{_host}:{_port}/{_db}"

_engine = create_engine(DB_URL)

Session = sessionmaker(bind=_engine)

