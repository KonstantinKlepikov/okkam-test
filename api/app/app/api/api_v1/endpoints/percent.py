from fastapi import (
    APIRouter,
    status,
    Depends,
    HTTPException,
    BackgroundTasks,
    Query,
        )
from app.config import settings


router = APIRouter()
