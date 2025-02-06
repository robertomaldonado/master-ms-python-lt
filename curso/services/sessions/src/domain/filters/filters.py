from sqlalchemy import Update
from sqlalchemy.orm import Query

from src.models.session import Session


class Filters:
    access_token: str | None
    refresh_token: str | None
    user_id: int | None


    def __init__(self, **kwargs):
        self.access_token = kwargs.get("access_token", None)
        self.refresh_token = kwargs.get("refresh_token", None)
        self.user_id = kwargs.get("user_id", None)


    def apply(self, query: Query | Update) -> Query | Update:
        if self.user_id:
            query = query.filter(Session.user_id == self.user_id)

        if self.access_token:
            query = query.filter(Session.access_token == self.access_token)

        if self.refresh_token:
            query = query.filter(Session.refresh_token == self.refresh_token)

        return query