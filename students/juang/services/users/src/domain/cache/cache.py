from redis import Redis


class Cache:
    db: Redis

    def __init__(self, db: Redis):
        self.db = db

    def set(self, key: str, value: str, expire: int = 0) -> None:
        self.db.set(key, value, ex=expire)

    def get(self, key: str) -> str:
        return self.db.get(key)

    def delete(self, key: str) -> None:
        self.db.delete(key)

    def exists(self, key: str) -> bool:
        return self.db.exists(key)

    def expire(self, key: str, seconds: int) -> None:
        self.db.expire(key, seconds)
