from .dtos import DeleteUserRequest, DeleteUserResponse


def delete_user(request: DeleteUserRequest) -> DeleteUserResponse:
  userExists = True  # Check if user exists based on id
  if userExists:
    return DeleteUserResponse(
        id=request,
        isDeleted=True
    )
  else:
    return DeleteUserResponse(
        id=request,
        isDeleted=False
    )
