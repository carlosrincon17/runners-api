"""Adding new user columns

Revision ID: d8e2666ce98e
Revises: 1fddf79b2d48
Create Date: 2021-03-18 21:50:53.091153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8e2666ce98e'
down_revision = '1fddf79b2d48'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users', sa.Column('state', sa.String(50))
    )
    op.drop_column(
        'users', 'country'
    )
    op.add_column(
        'registration_types', sa.Column('color', sa.String(50))
    )


def downgrade():
    pass
