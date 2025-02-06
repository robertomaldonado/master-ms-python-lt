from fastapi import HTTPException

from src.domain.filters.filters import Filters
from src.domain.filters.options import Options
from src.domain.services.user import UserService
from src.routes.dtos.users import CreateUserRequest, UserResponse, DeleteUserResponse, ListAllUsersResponse, \
    SearchUsersResponse, PaginationMetadata, UpdateUserRequest


class UsersController:
    def __init__(self, srv_users: UserService):
        self.srv_users = srv_users

    def create(self, request: CreateUserRequest) -> UserResponse:
        user = self.srv_users.create(
            email=request.email,
            username=request.username,
            password=request.password,
            app_version=request.app_version
        )

        return UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            app_version=user.app_version
        )

    def delete(self, user_id: int) -> DeleteUserResponse:
        user = self.srv_users.delete(user_id)

        return DeleteUserResponse(
            id=user.id,
            message="User deleted successfully",
        )

    def get(self, user_id: int) -> UserResponse:
        user = self.srv_users.get(user_id)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        return UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            app_version=user.app_version
        )

    def list_all(self) -> ListAllUsersResponse:
        users = self.srv_users.list_all()

        return ListAllUsersResponse(
            data=[UserResponse(
                id=user.id,
                email=user.email,
                username=user.username,
                app_version=user.app_version
            ) for user in users],
        )

    def search(
            self,
            page: int,
            limit: int,
            email: str | None,
            username: str | None,
            app_version: str | None,
    ) -> SearchUsersResponse:
        filters = Filters(
            email=email,
            username=username,
            app_version=app_version
        )

        options = Options(
            page=page,
            limit=limit
        )

        users, total, pages, current_page = self.srv_users.search(filters, options)

        return SearchUsersResponse(
            data=[
                UserResponse(
                    id=user.id,
                    email=user.email,
                    username=user.username,
                    app_version=user.app_version
                ) for user in users
            ],
            meta=PaginationMetadata(
                total=total,
                page=current_page,
                pages=pages,
                limit=limit
            )
        )

    def update(self, user_id: int, data: UpdateUserRequest) -> UserResponse:
        user = self.srv_users.update(
            user_id=user_id,
            email=data.email,
            username=data.username,
            app_version=data.app_version
        )

        return UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            app_version=user.app_version
        )
