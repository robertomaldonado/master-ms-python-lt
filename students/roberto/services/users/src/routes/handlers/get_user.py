from .dtos import UserResponse, GetUserRequest


def get_user(request: GetUserRequest) -> UserResponse:
  userExists = True  # Check if user exists based on id
  if userExists:
    return UserResponse(id=request,
                        email="Asociated mail",
                        username="Asociated username",
                        app_version="v0.0"
                        )
  else:
    return UserResponse(
        id=0,
        email="",
        username=""
    )
