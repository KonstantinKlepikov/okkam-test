from sqlalchemy import Column, Integer, Enum
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from app.schemas.constraint import Sex


class Respondents(Base):
    """Respondents db model
    """
    respondent = Column(Integer, unique=True, index=True)
    sex = Column(Enum(Sex))
    age = Column(Integer)
    weights = relationship("Weights", back_populates="owner")
