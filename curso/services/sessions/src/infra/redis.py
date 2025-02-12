from redis import Redis
from opentelemetry.instrumentation.redis import RedisInstrumentor

from .environment import envs

RedisInstrumentor().instrument()

instance = Redis(
    host=envs.get("REDIS_HOST"),
    port=envs.get_int("REDIS_PORT"),
    db=envs.get_int("REDIS_DB"),
)
