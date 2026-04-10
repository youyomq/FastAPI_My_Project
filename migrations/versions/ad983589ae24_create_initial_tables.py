"""create initial tables

Revision ID: ad983589ae24
Revises: 
Create Date: 2026-04-06 13:41:51.763712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'ad983589ae24'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade() -> None:
    op.drop_table('users')

