from fastapi import FastAPI

from app.endpoints import router


def include_router(app: FastAPI) -> FastAPI:
    app.include_router(router)
    return app


def start_app() -> FastAPI:
    app = FastAPI()
    app = include_router(app)
    return app


app = start_app()
