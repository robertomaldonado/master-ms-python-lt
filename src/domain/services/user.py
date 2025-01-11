import json
import math
from typing import Optional, List, Tuple

from src.domain.cache.cache import Cache
from src.domain.filters.filters import Filters
from src.domain.filters.options import Options
from src.models import User
from src.domain.repositories.user import UserRepository
from src.infra.logger import log


class UserService:
    def __init__(self, repo: UserRepository, cache: Cache):
        self.repo = repo
        self.cache = cache

    def create(self, email: str, username: str, password: str, app_version: Optional[str] = None) -> User:
        if len(password) < 8:
            raise ValueError('Password must have at least 8 characters')

        if not app_version:
            app_version = 'undefined'

        email = email.lower()

        return self.repo.create(
            email=email,
            username=username,
            password=password,
            app_version=app_version
        )

    def update(self, user_id: int, email:Optional[str], username:Optional[str], app_version:Optional[str]) -> User:
        user = self.repo.update(user_id, email, username, app_version)

        if self.cache.exists(f"urs:{user_id}"):
            self.cache.delete(f"urs:{user_id}")

        return user

    def delete(self, user_id: int) -> User:
        user = self.repo.delete(user_id)

        if self.cache.exists(f"urs:{user_id}"):
            self.cache.delete(f"urs:{user_id}")

        return user

    def get(self, user_id: int) -> User:
        if self.cache.exists(f"urs:{user_id}"):
            cached_user = self.cache.get(f"urs:{user_id}")
            dict_user = json.loads(cached_user)

            log.info(f"User {user_id} found in cache")

            return User.from_dict(dict_user)

        user = self.repo.get(user_id)

        user_dict = user.to_dict()
        log.info(f"User {user_id} found in database", extra={"user": user_dict})

        self.cache.set(f"urs:{user_id}", json.dumps(user.to_dict()), expire=60)

        log.info(f"User {user_id} not found in cache")

        return user

    def list_all(self) -> List[User]:
        return self.repo.list_all()

    def search(self, filters: Filters, options: Options = Options(limit=10, page=1)) -> Tuple[List[User], int, int, int]:
        """
        Search for users based on the provided filters and options
        :param filters:
        :param options:
        :return Tuple[List[User], int, int]: users, total, pages, current_page
        """

        total = self.repo.count(filters)
        pages = int(math.ceil(float(total) / float(options.limit)))
        page = options.page if options.page <= pages else pages
        offset = (page - 1) * options.limit

        if offset < 0:
            offset = 0

        users = self.repo.search(filters, options.limit, offset)

        return users, total, pages, page



