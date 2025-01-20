from fastapi import Depends
from sqlalchemy.orm import Session

from src.providers.infra.database import provide_db_session
from src.domain.repositories.sessions import SessionRepository


def provide_session_repository(db: Session = Depends(provide_db_session)) -> SessionRepository:
    return SessionRepository(db)
