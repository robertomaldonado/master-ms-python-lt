from src.infra.redis import instance


def provide_redis():
    return instance
