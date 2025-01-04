from .dtos import ListUserResponse, PaginationMetadata, UserResponse


def list_users() -> ListUserResponse:
    return ListUserResponse(
        data=[
            UserResponse(id=1, email="test@test.com", username="test", app_version="1.0.0"),
        ],
        meta=PaginationMetadata(
            total=1,
            page=1,
            limit=10
        )
    )
