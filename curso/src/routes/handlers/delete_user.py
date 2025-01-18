from .dtos import DeleteUserResponse
from src.domain.services.user import UserService


def delete_user(user_id: int, user_service: UserService) -> DeleteUserResponse:
    user = user_service.delete(user_id)

    return DeleteUserResponse(
        id=user.id,
        message="User deleted successfully",
    )