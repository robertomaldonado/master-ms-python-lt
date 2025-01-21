from .dtos import ListUserResponse, PaginationMetadata, UserResponse

def list_users() -> ListUserResponse:
    return ListUserResponse(
        data=[
            UserResponse(
                id=1, 
                email="jtavo@gmail.com", 
                username='test', 
                password='dsldlsdjl', 
                app_version='1.0.1'),
        ],
        meta=PaginationMetadata(
            total=1,
            page=1,
            limit=10
        )
    )