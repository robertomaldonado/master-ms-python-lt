from .dtos import CreateUserRequest, UserResponse


def create_user(request: CreateUserRequest) -> UserResponse:
  return UserResponse(
      id=1,
      email=request.email,
      username=request.username,
      app_version=request.app_version
  )
