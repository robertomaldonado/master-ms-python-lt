from src.infra.database import SessionLocal


def provide_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
