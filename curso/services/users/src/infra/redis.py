from redis import Redis

from .environment import envs


instance = Redis(
    host=envs.get("REDIS_HOST"),
    port=envs.get_int("REDIS_PORT"),
    db=envs.get_int("REDIS_DB"),
)
