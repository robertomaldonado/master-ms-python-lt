from src.infra.environment import envs
from src.libs.sessions import Client


def provide_sessions_client() -> Client:
    base_url = envs.get('SESSIONS_API_URL')
    api_key = envs.get('SESSIONS_API_KEY')

    return Client(
        base_url=base_url,
        api_key=api_key
    )
