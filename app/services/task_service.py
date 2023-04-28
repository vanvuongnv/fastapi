from datetime import datetime
from uuid import UUID
from sqlalchemy import func
from sqlalchemy.orm import Session
from schemas.task import Task

from models.task_model import TaskModel

def add_task(owner: UUID,
             model: TaskModel,
             db: Session):
    task = Task(**model.dict())
    task.owner_id = owner
    task.created_at = datetime.utcnow()
    task.updated_at = datetime.utcnow()
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_by_user(owner: UUID,
                    page: int,
                    size: int,
                    keyword: str,
                    db: Session):
    query = db.query(Task)
    query = query.filter(Task.owner_id == owner)
    if keyword is not None:
        query = query.filter(Task.summary.like(f"{keyword}%"))

    query = query.order_by(Task.created_at)
    query = query.offset((page-1)*size).limit(size)
    return query.all()

def count_tasks_by_user(owner: UUID,
                    keyword: str,
                    db: Session):
    query = db.query(Task)
    query = query.filter(Task.owner_id == owner)
    if keyword is not None:
        query = query.filter(Task.summary.like(f"{keyword}%"))

    query = query.with_entities(func.count(Task.id))
    return query.scalar()

def get_task_by_id(owner: UUID, task_id: UUID, db: Session):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == owner).first()
    return task

def edit_task(owner: UUID,
              task_id: UUID,
              model: TaskModel,
              db: Session):
    task = get_task_by_id(owner, task_id, db)
    if task is None:
        return False
    
    task.description = model.description
    task.priority = model.priority
    task.status = model.status
    task.summary = model.summary
    task.updated_at = datetime.utcnow()

    db.add(task)
    db.commit()
    db.refresh(task)

    return True

def delete_task_by_id(owner: UUID, task_id: UUID, db: Session):
    task = get_task_by_id(owner, task_id, db)
    if task is None:
        return False
    db.delete(task)
    db.commit()
    return True