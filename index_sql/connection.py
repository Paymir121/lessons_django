from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from index_sql.inid_data_django_orm import models as dm

class DBConnection:
    db_config: dict = {
        "drivername": "postgresql+psycopg2",
        "username": "postgres",
        "password": "456852",
        "host": "localhost",
        "database": "postgres",
        "port": 5432,
    }
    url_object: URL = URL.create(**db_config)
    engine = create_engine(url_object, echo=True)  # echo=True для логирования SQL
    dm.Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    print("DBC.1: Database connected")

if __name__ == '__main__':
    db_conn = DBConnection()
    print("DBC.2: Done. Таблицы созданы")