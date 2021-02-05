"""Added table users

Revision ID: 3d2ecb75b632
Revises: 
Create Date: 2021-01-31 22:17:56.912880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d2ecb75b632'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('first_name', sa.String(200), nullable=False),
        sa.Column('last_name', sa.String(200)),
        sa.Column('email', sa.String(255), unique=True),
        sa.Column('hashed_password', sa.String(255)),
        sa.Column('is_active', sa.Boolean),
        sa.Column('document_number', sa.String(10)),
        sa.Column('phone_number', sa.String(20)),
        sa.Column('birth_date', sa.Date),
    )


def downgrade():
    op.drop_table('users')
