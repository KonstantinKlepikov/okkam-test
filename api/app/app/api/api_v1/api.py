from app.api.api_v1.endpoints import percent
from fastapi import APIRouter


api_router = APIRouter()

api_router.include_router(
    percent.router, prefix="/percent", tags=['percent', ]
        )
