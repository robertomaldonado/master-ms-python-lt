from fastapi import HTTPException

from src.routes.handlers.dtos import UserResponse
from src.domain.services.user import UserService


def get_user(user_id: int, user_service: UserService) -> UserResponse:
    user = user_service.get(user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        app_version=user.app_version
   )