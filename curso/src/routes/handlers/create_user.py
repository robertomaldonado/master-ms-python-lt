from src.routes.handlers.dtos import CreateUserRequest, UserResponse
from src.domain.services.user import UserService


def create_user(request: CreateUserRequest, user_service: UserService) -> UserResponse:
    user = user_service.create(
        email=request.email,
        username=request.username,
        password=request.password,
        app_version=request.app_version
    )

    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        app_version=user.app_version
    )