"""Adding registration types data

Revision ID: 1d58e7a1b913
Revises: f790cf39b21c
Create Date: 2021-03-13 21:17:53.247349

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date, DECIMAL

# revision identifiers, used by Alembic.
revision = '1d58e7a1b913'
down_revision = 'f790cf39b21c'


def upgrade():
    accounts_table = table(
        'registration_types',
        column('id', Integer),
        column('name', String),
        column('limits', String),
        column('description', String),
        column('amount', DECIMAL),
        column('status', String)
    )

    op.bulk_insert(
        accounts_table,
        [
            {
                'name': 'Opción 1',
                'status': 'ACTIVE',
                'description': 'MEDALLA + NÚMERO DEL CORREDOR + TULA',
                'limits': '',
                'amount': 35000
            },
            {
                'name': 'Opción 2',
                'status': 'ACTIVE',
                'description': 'MEDALLA + NÚMERO DEL CORREDOR + CAMISA FINISHER',
                'limits': '',
                'amount': 70000
            },
            {
                'name': 'Opción 3',
                'status': 'ACTIVE',
                'description': 'MEDALLA + NÚMERO DEL CORREDOR + CAMISA FINISHER',
                'limits': 'Solo para personas con situación de discapacidad',
                'amount': 50000
            },
        ]
    )


def downgrade():
    pass
