from fastapi import FastAPI, Request, Response, APIRouter
from fastapi.responses import PlainTextResponse
from prometheus_client import REGISTRY, CONTENT_TYPE_LATEST, generate_latest

from src.infra.http import path
from src.infra.environment import envs
from src.routes.router import router
from src.routes.sessions import router as sessions_router
from src.infra.middlewares.log_request import log_request
from src.infra.middlewares.metrics import MetricsMiddleware


prefix = envs.get("PATH_PREFIX", "")

app = FastAPI()
app.add_middleware(MetricsMiddleware)


@app.middleware("http")
async def log_request_mdlw(req: Request, next):
    return await log_request(req, next)


base_router = APIRouter()


@base_router.get(path(".health", prefix))
def health():
    return {"status": "ok"}


@base_router.get(path("/prometheus/metrics", prefix), response_class=PlainTextResponse)
def metrics():
    return Response(content=generate_latest(REGISTRY), media_type=CONTENT_TYPE_LATEST)


app.include_router(base_router)
app.include_router(router)
app.include_router(sessions_router)
