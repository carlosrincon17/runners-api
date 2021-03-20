"""Adding events

Revision ID: 1fddf79b2d48
Revises: 1f5b9c9bb79f
Create Date: 2021-03-14 08:56:38.275342

"""
from datetime import date

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date, DECIMAL


# revision identifiers, used by Alembic.
revision = '1fddf79b2d48'
down_revision = '1f5b9c9bb79f'


def upgrade():
    accounts_table = table(
        'events',
        column('id', sa.Integer),
        column('event_set', sa.Integer),
        column('distance', String),
        column('start_date', Date),
        column('end_date', Date),
        column('start_enrollment_date', Date),
        column('end_enrollment_date', Date),
        column('description', String),
    )

    op.bulk_insert(
        accounts_table,
        [
            {
                'event_set': 1,
                'distance': '5K',
                'description': 'Se debe agregar una descrición para la carrera de 5K.',
                'start_enrollment_date': date(year=2021, month=3, day=1),
                'end_enrollment_date': date(year=2021, month=6, day=30),
                'start_date': date(year=2021, month=8, day=5),
                'end_date': date(year=2021, month=8, day=8),
            },
            {
                'event_set': 1,
                'distance': '10K',
                'description': 'Se debe agregar una descrición para la carrera de 10K.',
                'start_enrollment_date': date(year=2021, month=3, day=1),
                'end_enrollment_date': date(year=2021, month=6, day=30),
                'start_date': date(year=2021, month=8, day=5),
                'end_date': date(year=2021, month=8, day=8),
            },
            {
                'event_set': 1,
                'distance': '20K',
                'description': 'Se debe agregar una descrición para la carrera de 20K.',
                'start_enrollment_date': date(year=2021, month=3, day=1),
                'end_enrollment_date': date(year=2021, month=6, day=30),
                'start_date': date(year=2021, month=8, day=5),
                'end_date': date(year=2021, month=8, day=8),
            },
        ]
    )


def downgrade():
    pass

