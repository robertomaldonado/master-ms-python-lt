from fastapi import Depends

from src.domain.repositories.sessions import SessionsRepository
from src.domain.services.sessions import SessionsService
from src.providers.domain.repositories.sessions import provide_sessions_repository


def provide_sessions_service(repo: SessionsRepository = Depends(provide_sessions_repository)) -> SessionsService:
    return SessionsService(repo)
