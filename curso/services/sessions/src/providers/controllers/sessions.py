from fastapi import Depends

from src.domain.services.sessions import SessionService
from src.routes.controllers.sessions import SessionsController
from src.providers.domain.services.sessions import provide_session_service


def provide_sessions_controller(srv_sessions: SessionService = Depends(provide_session_service)) -> SessionsController:
    return SessionsController(srv_sessions)
