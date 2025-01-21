from src.libs.sessions import Client, Session


class SessionsRepository:
    def __init__(self, client: Client):
        self.client = client

    def generate(self, user_id: int) -> Session:
        return self.client.generate(user_id)
