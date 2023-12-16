from pydantic import BaseModel
from datetime import date


class WeightDb(BaseModel):
    """Weight db model
    """
    date: date
    weight: float
    respondent: int
