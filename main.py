from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import router

ORIGINS = ["http://localhost", "http://localhost:8080", "herokuapp.com"]


def include_router(app: FastAPI) -> FastAPI:
    app.include_router(router)
    return app


def start_app() -> FastAPI:
    app = FastAPI()
    app = include_router(app)
    return app


app = start_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
