
from typing import Optional
from pydantic import BaseModel, Field

from models.task_state import TaskState

class TaskModel(BaseModel):
    summary: str
    description: Optional[str]
    status: TaskState = Field(default=TaskState.INITIAL)
    priority: int = Field(default=10)