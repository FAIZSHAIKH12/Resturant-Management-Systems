"""menu_item

Revision ID: e687af777a9a
Revises: 35c75071071e
Create Date: 2024-06-20 21:47:19.668736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e687af777a9a'
down_revision: Union[str, None] = '35c75071071e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.create_table('menu_item',
                  sa.Column('id',sa.Integer,nullable=False),
                  sa.Column('name', sa.String(100),nullable=False),
                  sa.Column('desc',sa.String(200),nullable=False),
                  sa.Column('price',sa.Integer(),nullable=False),
                  sa.Column('availability',sa.Boolean(),nullable=False),
                  sa.PrimaryKeyConstraint("id"),)
 

def downgrade() -> None:
    op.drop_table('menu_item')
