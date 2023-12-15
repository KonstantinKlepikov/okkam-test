from sqlalchemy import Column, ForeignKey, Integer, Float, Date, Enum
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


class Weights(Base):
    """Respondent weights db model
    """
    date = Column(Date, index=True)
    weight = Column(Float)
    respondent = Column(Integer, ForeignKey("respondents.respondent"))
    owner = relationship("Respondents", back_populates="weights")
