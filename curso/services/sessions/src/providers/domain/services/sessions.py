from fastapi import Depends

from src.domain.repositories.sessions import SessionRepository
from src.domain.services.sessions import SessionService
from src.providers.domain.repositories.sessions import provide_session_repository


def provide_session_service(repo: SessionRepository = Depends(provide_session_repository)) -> SessionService:
    return SessionService(repo)
