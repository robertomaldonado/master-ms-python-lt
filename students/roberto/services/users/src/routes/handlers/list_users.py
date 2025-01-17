
from .dtos import ListUsersResponse, PaginationMetadata, UserResponse


def list_users() -> ListUsersResponse:
  return ListUsersResponse(
      data=[
          UserResponse(
              id=1,
              email="t@t.c",
              username="Test",
              app_version="v0.0"
          )
      ],
      meta=PaginationMetadata(
          total=1,
          page=1,
          limit=10
      )
  )
