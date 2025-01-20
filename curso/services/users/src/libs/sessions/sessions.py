import httpx

from .dtos import Session
from src.infra.logger import log


class Client:
    base_url: str
    api_key: str

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key


    def generate(self, user_id: int) -> Session:
        url = f'{self.base_url}/'

        payload = {
            'user_id': user_id
        }

        headers = {
            "X-Api-Key": self.api_key
        }

        log.debug("generating session", user_id=user_id, url=url, headers=headers, payload=payload)

        response = httpx.post(url, json=payload, headers=headers)
        response.raise_for_status()

        return Session(**response.json())
