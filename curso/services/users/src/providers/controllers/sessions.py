from fastapi import Depends

from src.domain.services.sessions import SessionsService
from src.domain.services.user import UserService
from src.providers.domain.services.sessions import provide_sessions_service
from src.routes.controllers.session import SessionsController
from src.providers.domain.services.user import provide_user_service


def provide_sessions_controller(
        srv_users: UserService = Depends(provide_user_service),
        srv_sessions: SessionsService = Depends(provide_sessions_service),
) -> SessionsController:
    return SessionsController(
        srv_users=srv_users,
        srv_sessions=srv_sessions,
    )
