from pydantic import BaseModel


class Percent(BaseModel):
    """Percent of intersection of audience"""

    percent: float = 0.0
