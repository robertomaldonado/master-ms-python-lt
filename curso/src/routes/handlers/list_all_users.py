from src.routes.handlers.dtos import ListAllUsersResponse, UserResponse
from src.domain.services.user import UserService


def list_all_users(user_service: UserService) -> ListAllUsersResponse:
    users = user_service.list_all()

    return ListAllUsersResponse(
        data=[UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            app_version=user.app_version
        ) for user in users],
    )
