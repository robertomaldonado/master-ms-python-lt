from src.domain.filters.filters import Filters
from src.domain.filters.options import Options
from src.routes.handlers.dtos import SearchUsersResponse, UserResponse, PaginationMetadata
from src.domain.services.user import UserService

def search_users(
        user_service: UserService,
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

    users, total, pages, current_page = user_service.search(filters, options)

    return SearchUsersResponse(
        data=[UserResponse(
            id=user.id,
            email=user.email,
            username=user.username,
            app_version=user.app_version
        ) for user in users],
        meta=PaginationMetadata(
            total=total,
            page=current_page,
            pages=pages,
            limit=limit
        )
    )