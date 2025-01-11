from .dtos import UserResponse


def get_user(user_id: int) -> UserResponse:
    return UserResponse(
        id=user_id,
        email="test@email.com",
        username="test_user_name",
        app_version="some-version 1.0.0",
    )