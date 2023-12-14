from app.api.api_v1.endpoints import root
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(
    root.router, prefix="/root", tags=['root', ]
        )
