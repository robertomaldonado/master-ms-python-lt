from pydantic import BaseModel


class DeleteUserRequest(BaseModel):
  id: int


class DeleteUserResponse(BaseModel):
  id: int
  isDeleted: bool


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
