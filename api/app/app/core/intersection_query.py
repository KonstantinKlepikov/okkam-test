from fastapi import HTTPException
from app.schemas.scheme_respondents import RespondentQuery
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from app.schemas.constraint import Sex
from app.schemas.scheme_percent import Percent


class QueryFilter:
    """Build audience query
    """

    def __init__(
        self,
        a1: RespondentQuery,
        a2: RespondentQuery,
        sex: Sex,
        db: Session
            ) -> None:
        """Init and constraint

        Args:
            a1 (RespondentQuery): audience one
            a2 (RespondentQuery): audience two
            sex (Sex): respondent sex
            db (Session): db session
        """
        self.a1 = a1
        self.a2 = a2
        self.sex = sex
        self._check_age()
        self._check_intersection_range()
        self.db = db

    def _check_age(self) -> None:
        """Check is age range correct

        Raises:
            HTTPException: wrong range
        """
        if (self.a1.agefrom > self.a1.ageto) or (self.a2.agefrom > self.a2.ageto):
            raise HTTPException(
                status_code=400,
                detail="Agefrom great than ageto. Must be less or equal."
                    )
        return

    def _check_intersection_range(self) -> None:
        """Check range intersection

        Raises:
            HTTPException: wrong range
        """

        if (self.a1.agefrom > self.a2.ageto) or (self.a2.agefrom > self.a1.ageto):
            raise HTTPException(
                status_code=400,
                detail="Range of ages not intersected"
                    )
        return

    def query(self) -> Percent:
        """Get query from db with parameters

        Example of query:

        SELECT SUM(aw2) / SUM(aw1) percent
        FROM (
            SELECT r1.respondent, AVG(w1.weight) aw1
            FROM respondents r1
            JOIN weights w1 ON (r1.respondent = w1.respondent)
            WHERE r1.age BETWEEN 1 and 20
            AND r1.sex = 'M'
            GROUP BY r1.respondent, r1.age, r1.sex
        ) ar1
        LEFT JOIN (
            SELECT r2.respondent, AVG(w2.weight) aw2
            FROM respondents r2
            JOIN weights w2 ON (r2.respondent = w2.respondent)
            WHERE r2.age BETWEEN 18 and 30
            AND r2.sex = 'M'
            GROUP BY r2.respondent, r2.age, r2.sex
        ) ar2
        ON (ar1.respondent = ar2.respondent)

        Returns:
            Percent: _percent of intersection
        """

        result = self.db.execute(
            text(
                "SELECT SUM(aw2) / SUM(aw1) percent "
                "FROM ( "
                "SELECT r1.respondent, AVG(w1.weight) aw1 "
                "FROM respondents r1 "
                "JOIN weights w1 ON (r1.respondent = w1.respondent) "
                "WHERE r1.age BETWEEN :a1from and :a1to "
                "AND r1.sex = :sex "
                "GROUP BY r1.respondent, r1.age, r1.sex"
                ") ar1 "
                "LEFT JOIN ( "
                "SELECT r2.respondent, AVG(w2.weight) aw2 "
                "FROM respondents r2 "
                "JOIN weights w2 ON (r2.respondent = w2.respondent) "
                "WHERE r2.age BETWEEN :a2from and :a2to "
                "AND r2.sex = :sex "
                "GROUP BY r2.respondent, r2.age, r2.sex "
                ") ar2 "
                "ON (ar1.respondent = ar2.respondent) "
                    ),
            {
                'a1from': self.a1.agefrom,
                'a1to': self.a1.ageto,
                'a2from': self.a2.agefrom,
                'a2to': self.a2.ageto,
                'sex': self.sex.name
                    }
                ).first()
        if result:
            return Percent(percent=result[0])
        else:
            return Percent()
