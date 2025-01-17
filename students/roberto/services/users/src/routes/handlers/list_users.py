from pydantic import BaseModel
from typing import List, Dict


class PaginationMetadata(BaseModel):
  total: int
  page: int
  limit: int


class ListUsersResponse(BaseModel):
  data: List[Dict]
  meta: PaginationMetadata


def list_users() -> ListUsersResponse:
  return ListUsersResponse(
      data=[
          {
              "id": 1,
              "email": "yhour@email.com"
          }
      ],
      meta=PaginationMetadata(
          total=1,
          page=1,
          limit=10
      )
  )
