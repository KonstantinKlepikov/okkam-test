from sqlalchemy.orm import Session
from app.crud.crud_base import CRUDBase
from app.models.model_respondents import Respondents
from app.schemas.scheme_respondents import RespondentDb


class CRUDRespondents(CRUDBase[
    Respondents,
    RespondentDb,
    RespondentDb]
        ):
    """CRUD respondent"""

    def get_by_respondent(
        self,
        db: Session, respondent: int
            ) -> Respondents | None:
        """Get respondent by db respondent number

        Args:
            db (Session): session
            respondent (int): respondent number

        Returns:
            ModelType | None: query result
        """
        return db.query(self.model).filter(
            self.model.respondent == respondent
                ).first()


respondents = CRUDRespondents(Respondents)
