
from uuid import UUID
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from routers.error import http_forbiden
from schemas.user import User
from services.auth_service import token_interceptor
from models.CompanyModel import CompanyModel
from schemas.company import Company
from database import get_db_context
from services import company_service
from routers.error import http_exception, http_forbiden, http_badrequest
router = APIRouter(prefix='/api/v1/companies', tags=['Companies'])

@router.get('')
async def index(db: Session = Depends(get_db_context)):
    items = company_service.get_companies(db)
    return items

@router.get('/{company_id}')
async def getById(company_id: UUID, db: Session = Depends(get_db_context)):
    item = company_service.get_company_by_id(company_id, db)
    if item is not None:
        return item
    raise http_exception()

@router.post('', status_code=status.HTTP_201_CREATED)
async def addCompany(request: CompanyModel, 
                     user: User = Depends(token_interceptor),
                     db: Session = Depends(get_db_context)):
    if not user.is_admin:
        raise http_forbiden()
    
    company = company_service.add_company(request, db)

    return company

@router.put('/{company_id}')
async def updateCompany(company_id: UUID,
                     request: CompanyModel, 
                     user: User = Depends(token_interceptor),
                     db: Session = Depends(get_db_context)):
    if not user.is_admin:
        raise http_forbiden()
    
    result = company_service.edit_company(company_id, request, db)

    if result == False:
        raise http_badrequest()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/{company_id}')
async def deleteCompany(company_id: UUID,
                     user: User = Depends(token_interceptor),
                     db: Session = Depends(get_db_context)):
    if not user.is_admin:
        raise http_forbiden()
    
    result = company_service.delete_company(company_id, db)
    
    if result == False:
        raise http_badrequest()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)