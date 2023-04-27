"""initial data

Revision ID: 219720ccf0d7
Revises: 3326c7f6c56b
Create Date: 2023-04-27 22:17:26.299787

"""
from datetime import datetime
from uuid import uuid4
from alembic import op
import sqlalchemy as sa

from services.hash_service import get_password_hash
from settings import ADMIN_DEFAULT_PASSWORD

# revision identifiers, used by Alembic.
revision = '219720ccf0d7'
down_revision = '3326c7f6c56b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    meta = sa.MetaData()
    meta.reflect(only=('companies','users'),bind=op.get_bind())
    companies_table = sa.Table('companies', meta)
    users_table = sa.Table('users', meta)
    
    company_id = uuid4()
    op.bulk_insert(companies_table, [
        {
            "id": company_id,
            "name": "Nash Tech",
            "description": "Nash Tech Company - HCM City",
            "mode": 1,
            "rating": 5
        }
    ])

    op.bulk_insert(users_table, [
        {
            "id": uuid4(),
            "email": "fastapi_tour@sample.com", 
            "username": "fa_admin",
            "hash_password": get_password_hash(ADMIN_DEFAULT_PASSWORD),
            "first_name": "FastApi",
            "last_name": "Admin",
            "is_active": True,
            "is_admin": True,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "company_id": company_id
        }
    ])


def downgrade() -> None:
    pass
