from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Time, Uuid
from app.models.TaskState import TaskState
from database import Base
from schemas.base_entity import BaseEntity
from sqlalchemy.orm import relationship


class Task(Base, BaseEntity):
    __tablename__ = "tasks"

    summary = Column(String, nullable=False)
    description = Column(String)
    status = Column(Enum(TaskState), nullable=False, default=TaskState.INITIAL)
    priority = Column(Integer, default=10)
    owner_id = Column(Uuid, ForeignKey("users.id"), nullable=False)
    created_at = Column(Time)
    updated_at = Column(Time)

    user = relationship('User')