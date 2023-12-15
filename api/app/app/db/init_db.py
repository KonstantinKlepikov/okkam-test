from sqlalchemy.orm import Session
from app.crud import crud_base
from app.config import settings


def init_db(db: Session) -> None:
    """Init database data for def tests

    make sure all SQL Alchemy models are imported
    (app.db.base) before initializing DBю Щtherwise, SQL
    Alchemy might fail to initialize relationships properly
    for more details:
    https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

    Args:
        db (Session): database session
    """
