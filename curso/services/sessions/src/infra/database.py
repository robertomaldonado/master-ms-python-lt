from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor

from .environment import envs


DATABASE_URL = envs.get("POSTGRES_URL")

engine = create_engine(DATABASE_URL, echo=True)
SQLAlchemyInstrumentor().instrument(engine=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
