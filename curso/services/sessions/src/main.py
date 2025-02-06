from fastapi import FastAPI, Request

from src.routes.router import router
from src.infra.middlewares.api_key import api_key
from src.infra.middlewares.log_request import log_request

app = FastAPI()

@app.middleware("http")
async def log_request_mdlw(req: Request, next):
    return await log_request(req, next)

@app.middleware("http")
async def verify_api_key(request: Request, call_next):
    return await api_key(request, call_next)


app.include_router(router)
