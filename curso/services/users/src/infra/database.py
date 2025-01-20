from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .environment import envs


DATABASE_URL = envs.get("POSTGRES_URL")

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
