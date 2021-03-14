"""Added Events, Category, Test tables

Revision ID: 276e098df8ca
Revises: 3d2ecb75b632
Create Date: 2021-02-03 21:17:05.130587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '276e098df8ca'
down_revision = '3d2ecb75b632'


def upgrade():
    op.create_table(
        'events',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('event_set', sa.Integer),
        sa.Column('distance', sa.String(255)),
        sa.Column('start_date', sa.Date),
        sa.Column('end_date', sa.Date),
        sa.Column('start_enrollment_date', sa.Date),
        sa.Column('end_enrollment_date', sa.Date),
        sa.Column('description', sa.Text),
    )


def downgrade():
    op.drop_table('events')
