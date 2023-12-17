from pydantic import BaseModel
from typing import Literal
from pydantic import Field
from app.schemas.constraint import Sex


class RespondentQuery(BaseModel):
    """Respondent query parameters
    """
    agefrom: int = Field(default=0, ge=0, le=150)
    ageto: int = Field(default=150, ge=0, le=150)

    class Config:
        json_schema_extra = {
            "example": {
                'agefrom': 1,
                'ageto': 16,
                    }
                }


class PercentParams(BaseModel):
    """Percent params
    """
    sex: Sex
    audience1: RespondentQuery
    audience2: RespondentQuery


class RespondentDb(BaseModel):
    """Respondent db model
    """
    respondent: int
    sex: Literal['M', 'W']
    age: int

    class Config:
        json_schema_extra = {
            "example": {
                'respondent': 0,
                'sex': 'M',
                'age': 16,
                    }
                }
