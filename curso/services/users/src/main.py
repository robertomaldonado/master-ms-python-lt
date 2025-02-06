from fastapi import FastAPI, Request
from src.routes.router import router
from src.routes.sessions import router as sessions_router
from src.infra.middlewares.log_request import log_request

app = FastAPI()


@app.middleware("http")
async def log_request_mdlw(req: Request, next):
    return await log_request(req, next)


app.include_router(router)
app.include_router(sessions_router)
