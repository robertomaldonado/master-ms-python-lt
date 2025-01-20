from typing import Optional

from src.models.user import User


class Filters:
    username: Optional[str]
    email: Optional[str]
    app_version: Optional[str]

    def __init__(self, username: Optional[str] = None, email: Optional[str] = None, app_version: Optional[str] = None):
        self.username = username
        self.email = email
        self.app_version = app_version

    def __repr__(self):
        return f"<Filters(username={self.username}, email={self.email}, app_version={self.app_version})>"

    def apply(self, query):
        if self.username:
            query = query.filter(User.username.ilike(f"%{self.username}%"))

        if self.email:
            query = query.filter(User.email.ilike(f"%{self.email}%"))

        if self.app_version:
            query = query.filter(User.app_version.ilike(f"%{self.app_version}%"))

        return query