from .dtos import UpdateUserRequest, UserResponse


def update_user(user_id: int, data: UpdateUserRequest) -> UserResponse:
    return UserResponse(
        id=user_id,
        email=data.email if data.email else "no_change@test.com",
        username=data.username if data.username else "no_change_username",
        app_version=data.app_version if data.app_version else "no_change_version",
    )