from fastapi import Depends

from src.libs.sessions import Client
from src.domain.repositories.sessions import SessionsRepository
from src.providers.libs.sessions import provide_sessions_client


def provide_sessions_repository(client: Client = Depends(provide_sessions_client)) -> SessionsRepository:
    return SessionsRepository(client)
