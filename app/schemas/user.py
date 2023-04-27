from sqlalchemy import Boolean, Column, ForeignKey, Time, String, Uuid
from schemas.company import Company
from schemas.base_entity import BaseEntity
from sqlalchemy.orm import relationship
from database import Base

class User(Base, BaseEntity):
    __tablename__ = "users"

    email = Column(String, nullable=False)
    username= Column(String, nullable=False)
    first_name= Column(String, nullable=True)
    last_name= Column(String)
    hash_password= Column(String, nullable=False)
    is_active= Column(Boolean, default=True)
    is_admin= Column(Boolean, default=False)
    company_id= Column(Uuid, ForeignKey("companies.id"), nullable=False)
    created_at = Column(Time)
    updated_at = Column(Time)

    company = relationship(Company)