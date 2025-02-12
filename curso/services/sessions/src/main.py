from fastapi import FastAPI, Request

from src.routes.router import router
from src.infra.environment import envs
from src.infra.otel import instrument_app
from src.infra.middlewares.api_key import APIKeyMiddleware
from src.infra.middlewares.log_request import LogRequestMiddleware
from src.infra.middlewares.metrics import MetricsMiddleware

app = FastAPI()
instrument_app(app)

app.add_middleware(LogRequestMiddleware)
app.add_middleware(APIKeyMiddleware)
app.add_middleware(MetricsMiddleware)

prefix = envs.get("PATH_PREFIX", "")

app.include_router(router)
