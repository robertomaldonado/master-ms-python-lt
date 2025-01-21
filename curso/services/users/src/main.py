from fastapi import FastAPI
from src.routes.router import router
from src.routes.sessions import router as sessions_router

app = FastAPI()

app.include_router(router)
app.include_router(sessions_router)
