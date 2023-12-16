from typing import Any, Generic, Type, TypeVar
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.base_class import Base


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model

    def get(self, db: Session, id: Any) -> ModelType | None:
        """Get respondent by db id

        Args:
            db (Session): session
            id (Any): db id

        Returns:
            ModelType | None: query result
        """
        return db.query(self.model).filter(self.model.id == id).first()

    def get_many(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        """Get many respondents with skip and limit parameters

        Args:
            db (Session): session_
            skip (int, optional): Defaults to 0.
            limit (int, optional): Defaults to 100.

        Returns:
            list[ModelType]: query result
        """
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
        """Create respondent

        Args:
            db (Session): session_
            obj_in (CreateSchemaType): respondent data

        Returns:
            ModelType: db model
        """
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self,
        db: Session,
        *,
        db_obj: ModelType,
        obj_in: UpdateSchemaType | dict[str, Any]
    ) -> ModelType:
        """Update respondent

        Args:
            db (Session): session
            db_obj (ModelType): _model to update
            obj_in (UpdateSchemaType | dict[str, Any]): respondent data

        Returns:
            ModelType: db model
        """
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, *, id: int) -> ModelType:
        """Remove respondent

        Args:
            db (Session): session
            id (Any): db id

        Returns:
            ModelType: db model
        """
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
