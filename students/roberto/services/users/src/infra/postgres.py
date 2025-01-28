from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL= "postgresql://root:root@localhost:xxxx/postgres"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

