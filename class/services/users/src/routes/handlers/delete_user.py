from .dtos import DeleteUserResponse


def delete_user(user_id: int) -> DeleteUserResponse:
    return DeleteUserResponse(
        id=user_id,
        message="User deleted successfully",
   )