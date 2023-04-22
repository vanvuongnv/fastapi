"""Added company table

Revision ID: 42d0b8af88e5
Revises: 
Create Date: 2023-04-22 22:58:54.873648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42d0b8af88e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'companies',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String,nullable=True),
        sa.Column('mode', sa.Numeric, nullable=False),
        sa.Column('rating', sa.Numeric, nullable=False, default=0)
    )

def downgrade() -> None:
    op.drop_table('companies')
