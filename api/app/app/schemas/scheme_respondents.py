from pydantic import BaseModel
from typing import Literal


class RespondentDb(BaseModel):
    """Respondent db model
    """
    respondent: int
    sex: Literal['M', 'W']
    age: int
