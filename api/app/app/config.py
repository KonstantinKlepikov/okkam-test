import toml
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from typing import Type
from app.schemas.scheme_error import (
    HttpErrorMessage,
    HttpError400,
    HttpError404,
    HttpError409,
    HttpError429,
        )


ErrorType = dict[int, dict[str, Type[HttpErrorMessage]]]
poetry_data = toml.load('pyproject.toml')['tool']['poetry']


class Settings(BaseSettings):
    # api vars
    API_V1: str = "/api/v1"

    # db settings
    DATABASE_URL: SecretStr

    # open-api settings
    title: str = poetry_data['name']
    descriprion: str = poetry_data['description']
    version: str = poetry_data['version']
    openapi_tags: list = [
        {
            "name": "percent",
            "description": "percent api",
        },
    ]
    ERRORS: ErrorType = {
        400: {'model': HttpError400},
        404: {'model': HttpError404},
        409: {'model': HttpError409},
        429: {'model': HttpError429}
            }


settings = Settings()
