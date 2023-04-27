"""add tasks table

Revision ID: 3326c7f6c56b
Revises: 70f5bea2f911
Create Date: 2023-04-27 21:59:34.500251

"""
from alembic import op
import sqlalchemy as sa

from models.TaskState import TaskState


# revision identifiers, used by Alembic.
revision = '3326c7f6c56b'
down_revision = '70f5bea2f911'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'tasks',
        sa.Column('id', sa.UUID, nullable=False, primary_key=True),
        sa.Column('summary', sa.String, nullable=False),
        sa.Column('description', sa.String),
        sa.Column('status', sa.Enum(TaskState), nullable=False, default=TaskState.INITIAL),
        sa.Column('priority', sa.Integer, default=10),
        sa.Column('owner_id', sa.UUID, nullable=False),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime)
    )
    op.create_foreign_key('fk_task_user', 'tasks', 'users', ['owner_id'], ['id'])

def downgrade() -> None:
    op.drop_table('tasks')
