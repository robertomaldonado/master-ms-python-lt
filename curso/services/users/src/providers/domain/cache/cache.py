from fastapi import Depends

from src.providers.infra.redis import provide_redis
from src.domain.cache.cache import Cache


def provide_cache(redis=Depends(provide_redis)):
    return Cache(redis)
