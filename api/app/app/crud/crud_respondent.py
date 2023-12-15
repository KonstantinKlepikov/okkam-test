from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.percent import Respondents, Weights
from app.schemas.scheme_respondent import RespondentCreate, RespondentUpdate


class CRUDRespondent(CRUDBase[
    Respondents,
    RespondentCreate,
    RespondentUpdate]
        ):
    """CRUD percent"""


respondent = CRUDRespondent(Respondents)