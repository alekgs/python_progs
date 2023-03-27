import os
from dotenv import load_dotenv, dotenv_values
import sqlalchemy as sq
import sqlalchemy.orm as sqo


def connect_db():
    # загружаем переменные из файла .env для подключения к БД
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    p = {k: v for k, v in dotenv_values().items()}

    # строка подключения к БД
    DSN = f"{p['DB_TYPE']}://" \
          f"{p['USER']}:" \
          f"{p['PASSWORD']}@" \
          f"{p['SERVER_ADDR']}/{p['DB']}"
    engine = sq.create_engine(DSN)
    Session = sqo.sessionmaker(bind=engine)
    return engine, Session

