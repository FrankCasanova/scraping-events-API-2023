from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import router

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
    allow_origins=["*"],	
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
