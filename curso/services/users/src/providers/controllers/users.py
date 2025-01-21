from fastapi import Depends

from src.domain.services.user import UserService
from src.routes.controllers.users import UsersController
from src.providers.domain.services.user import provide_user_service


def provide_users_controller(srv_users: UserService = Depends(provide_user_service)) -> UsersController:
    return UsersController(srv_users)
