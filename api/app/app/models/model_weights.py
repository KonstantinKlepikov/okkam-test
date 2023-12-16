from sqlalchemy import Column, ForeignKey, Integer, Float, Date
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Weights(Base):
    """Respondent weights db model
    """
    date = Column(Date, index=True)
    weight = Column(Float)
    respondent = Column(Integer, ForeignKey("respondents.respondent"))
    owner = relationship("Respondents", back_populates="weights")
