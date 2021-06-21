"""added is admin field to user

Revision ID: 828bb246e9ef
Revises: d8e2666ce98e
Create Date: 2021-06-20 13:32:52.331948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '828bb246e9ef'
down_revision = 'd8e2666ce98e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users', sa.Column('is_admin', sa.Boolean)
    )


def downgrade():
    op.drop_column(
        'users', 'is_admin'
    )
