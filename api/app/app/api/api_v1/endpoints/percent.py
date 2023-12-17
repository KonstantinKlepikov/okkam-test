from fastapi import (
    APIRouter,
    status,
    Depends,
        )
from sqlalchemy.orm import Session
from app.db.session import get_session
from app.core.intersection_query import QueryFilter
from app.schemas.scheme_percent import Percent
from app.schemas.scheme_respondents import PercentParams
from app.config import settings


router = APIRouter()


@router.post(
    "/getPercent",
    response_model=Percent,
    status_code=status.HTTP_200_OK,
    summary='Intersection of audience',
    response_description="Intersection of two audience, "
    "cfiltered by respondents age range",
    responses=settings.ERRORS
    )
def read_items(
    params: PercentParams,
    db: Session = Depends(get_session),
        ) -> Percent:
    """Get percent of intersection for two audience, filtered
    by respondents age range

    Sex 1 is a men, 2 a women

    Ageto and agefrom values are included in the range

    Age ranges must intersect, f.e. 1-12 and 12-120

    Age cant be less than 1 and great than 150.
    You can use none object - thi replaced by min or max range value.

    Returns:
        Percent: percent of intersection value
    """
    qf = QueryFilter(
        params.audience1,
        params.audience2,
        params.sex,
        db
            )
    return qf.query()
