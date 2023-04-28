from uuid import UUID
from sqlalchemy.orm import Session
from models.company_model import CompanyModel
from sqlalchemy import func

from schemas.company import Company

def get_companies(page: int,
                  size: int,
                  keyword: str,
                  db: Session):
    query = db.query(Company)
    if keyword is not None:
        query = query.filter(Company.name.like(f"{keyword}%"))
    query = query.order_by(Company.name)
    query = query.offset((page-1)*size).limit(size)
    return query.all()

def count_companies(keyword: str,
                  db: Session):
    query = db.query(Company)
    if keyword is not None:
        query = query.filter(Company.name.like(f"{keyword}%"))
    query = query.with_entities(func.count(Company.id))
    return query.scalar()
   

def get_company_by_id(id: UUID, db:Session):
    item = db.query(Company).filter(Company.id == id).first()
    return item

def add_company(model: CompanyModel, db: Session):
    company = Company(**model.dict())
    db.add(company)
    db.commit()
    db.refresh(company)
    return company

def edit_company(company_id: UUID, model: CompanyModel, db: Session):
    company = get_company_by_id(company_id, db)
    if company is None:
        return False
    
    company.description = model.description
    company.mode = model.mode
    company.name = model.name
    company.rating = model.rating

    db.add(company)
    db.commit()
    db.refresh(company)
    return True

def delete_company(company_id: UUID, db: Session):
    company = get_company_by_id(company_id, db)
    if company is None:
        return False
    
    db.delete(company)
    db.commit()
    return True