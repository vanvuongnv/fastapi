"""add users table

Revision ID: 70f5bea2f911
Revises: 42d0b8af88e5
Create Date: 2023-04-27 21:53:19.007517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70f5bea2f911'
down_revision = '42d0b8af88e5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.UUID, nullable=False,primary_key=True),
        sa.Column('email', sa.String, nullable=False),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('first_name', sa.String, nullable=True),
        sa.Column('last_name', sa.String),
        sa.Column('hash_password', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean, default=True),
        sa.Column('is_admin', sa.Boolean, default=False),
        sa.Column('company_id', sa.UUID, nullable=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )
    op.create_foreign_key('fk_user_company', 'users', 'companies', ['company_id'], ['id'])

def downgrade() -> None:
    op.drop_table('users')
