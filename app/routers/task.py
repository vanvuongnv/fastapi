
from uuid import UUID
from fastapi import APIRouter, Depends, Query, Response, status
from routers.error import http_exception, http_badrequest
from database import get_db_context
from schemas.user import User
from services.auth_service import token_interceptor
from sqlalchemy.orm import Session


from models.task_model import TaskModel
from services import task_service

router = APIRouter(prefix='/api/v1/tasks', tags=['Tasks'])

@router.post('', status_code=status.HTTP_201_CREATED)
async def add_task(request: TaskModel,
                   user: User = Depends(token_interceptor),
                   db: Session = Depends(get_db_context)):
    task = task_service.add_task(user.id, request, db)
    return task

@router.get('')
async def index(page: int = Query(ge=1, default=1), 
                size: int = Query(ge=1, le=50, default=10), 
                keyword: str = Query(default=None), 
                user: User = Depends(token_interceptor),
                db: Session = Depends(get_db_context)):
    items = task_service.get_tasks_by_user(user.id, page, size, keyword, db)
    total = task_service.count_tasks_by_user(user.id, keyword, db)
    return {
        "items": items,
        "pageInfo": {
            "total": total,
            "size": size,
            "page": page
        }
    }

@router.put('/{task_id}')
async def edit_task(task_id: UUID,
                    request: TaskModel,
                    user: User = Depends(token_interceptor),
                    db: Session = Depends(get_db_context)):
    result = task_service.edit_task(user.id, task_id, request, db)

    if result == False:
        raise http_badrequest()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get('/{task_id}')
async def get_task_by_id(task_id: UUID,
                    user: User = Depends(token_interceptor),
                    db: Session = Depends(get_db_context)):
    task = task_service.get_task_by_id(user.id, task_id, db)

    if task is None:
        raise http_exception()
    
    return task

@router.delete('/{task_id}')
async def delete_task_by_id(task_id: UUID,
                    user: User = Depends(token_interceptor),
                    db: Session = Depends(get_db_context)):
    result = task_service.delete_task_by_id(user.id, task_id, db)

    if result == False:
        raise http_badrequest()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)