"""Adding new event tables

Revision ID: f790cf39b21c
Revises: 276e098df8ca
Create Date: 2021-03-13 20:52:59.702273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f790cf39b21c'
down_revision = '276e098df8ca'


def upgrade():
    op.create_table(
        'registration_types',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(255)),
        sa.Column('limits', sa.Text),
        sa.Column('description', sa.Text),
        sa.Column('status', sa.String(255)),
        sa.Column('amount', sa.DECIMAL)
    )


def downgrade():
    op.drop_table('registration_types')
