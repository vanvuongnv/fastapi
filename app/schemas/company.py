from sqlalchemy import UUID, Column, Numeric, String
from database import Base
from schemas.base_entity import BaseEntity


class Company(Base, BaseEntity):
    __tablename__ = "companies"
    
    name = Column(String, nullable=False)
    description = Column(String,nullable=True)
    mode = Column(Numeric, nullable=False)
    rating = Column(Numeric, nullable=False, default=0)