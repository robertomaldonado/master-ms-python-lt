from fastapi import Depends

from src.domain.cache.cache import Cache
from src.domain.repositories.user import UserRepository
from src.domain.services.user import UserService
from src.providers.domain.cache.cache import provide_cache
from src.providers.domain.repositories.user import provide_user_repository


def provide_user_service(repo: UserRepository = Depends(provide_user_repository), cache: Cache = Depends(provide_cache)) -> UserService:
    return UserService(repo, cache)
