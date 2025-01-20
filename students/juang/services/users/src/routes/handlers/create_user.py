from .dtos import CreateUserRequest, UserResponse
def create_user(request: CreateUserRequest) -> UserResponse:
    generated_id = 1
    return UserResponse(
        id=generated_id,
        email=request.email,
        username=request.username,
        app_version=request.app_version
    )    