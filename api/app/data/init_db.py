import csv
from datetime import datetime
from app.db.session import SessionLocal
from app.db import base  # noqa: F401
from app.schemas.scheme_respondents import RespondentDb
from sqlalchemy import insert
from app.schemas.scheme_weights import WeightDb
from app.schemas.constraint import Sex
from app.models.model_respondents import Respondents
from app.models.model_weights import Weights
from app.crud.crud_respondents import respondents


def init_db() -> None:
    """Check and init dev database
    """
    db = SessionLocal()
    try:
        first = respondents.get_by_respondent(db, 1)
        if not first:

            with open('data/data.csv', newline='') as c:
                rows = csv.reader(c, delimiter=' ', quotechar=';')
                next(rows)

                count = set()
                r = []
                w = []
                for row in rows:
                    spl = row[0].split(";")
                    if spl[2] not in count:
                        r.append(RespondentDb(
                            respondent=spl[2],
                            sex=Sex(int(spl[3])).name,
                            age=spl[4]
                                ).model_dump())
                        count.add(spl[2])
                    w.append(WeightDb(
                        date=datetime.strptime(str(spl[1]), '%Y%m%d'),
                        weight=spl[5],
                        respondent=spl[2]
                            ).model_dump())

                db.execute(insert(Respondents), r)
                db.execute(insert(Weights), w)
                db.commit()

            print('Init dev db is done!')

    except Exception as e:
        print(e)

    db.close()


if __name__ == '__main__':
    init_db()
