"""Adding registration event table

Revision ID: 1f5b9c9bb79f
Revises: 1d58e7a1b913
Create Date: 2021-03-14 08:48:01.450820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5b9c9bb79f'
down_revision = '1d58e7a1b913'


def upgrade():
    op.create_table(
        'event_registrations',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('status', sa.String(255)),
        sa.Column('payment_evidence', sa.String(255)),
        sa.Column('payment_date', sa.DateTime),
        sa.Column('description', sa.Text),
        sa.Column('enrollment_date', sa.DateTime),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('event_id', sa.Integer, sa.ForeignKey('events.id')),
        sa.Column('registration_type_id', sa.Integer, sa.ForeignKey('registration_types.id')),
    )


def downgrade():
    op.drop_table('event_registrations')

