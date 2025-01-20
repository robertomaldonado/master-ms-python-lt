from .dtos import UserResponse, UpdateUserRequest


def update_user(request: UpdateUserRequest) -> UserResponse:
  return UserResponse(
      id=1,
      email=request.email,
      username=request.username,
      app_version=request.app_version
  )
