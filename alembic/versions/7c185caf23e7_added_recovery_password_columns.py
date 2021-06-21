"""added recovery password columns

Revision ID: 7c185caf23e7
Revises: 828bb246e9ef
Create Date: 2021-06-20 14:30:37.127809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c185caf23e7'
down_revision = '828bb246e9ef'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users', sa.Column('token_recovery', sa.String(20), nullable=True)
    )
    op.add_column(
        'users', sa.Column('last_recovery_date', sa.DateTime, nullable=True)
    )


def downgrade():
    op.drop_column(
        'users', 'token_recovery'
    )
    op.drop_column(
        'users', 'last_recovery_date'
    )

