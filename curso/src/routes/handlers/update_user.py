from .dtos import UpdateUserRequest, UserResponse
from src.domain.services.user import UserService


def update_user(user_id: int, data: UpdateUserRequest, user_service: UserService) -> UserResponse:
    user = user_service.update(
        user_id=user_id,
        email=data.email,
        username=data.username,
        app_version=data.app_version
    )

    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        app_version=user.app_version
    )