from fastapi import Depends
from sqlalchemy.orm import Session

from src.domain.repositories.user import UserRepository
from src.providers.infra.database import provide_db_session


def provide_user_repository(db: Session = Depends(provide_db_session)) -> UserRepository:
    return UserRepository(db)
