"""customer_info

Revision ID: 310251e91f1f
Revises: 
Create Date: 2024-06-20 20:22:07.317802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '310251e91f1f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
  op.create_table('user',
                  sa.Column('id',sa.Integer,nullable=False),
                  sa.Column('name', sa.String(50),nullable=False),
                  sa.Column('phone',sa.String(),nullable=False),
                  sa.Column('address',sa.String(200),nullable=False),
                  sa.Column('email', sa.String(50),nullable=False),
                  sa.Column('_password', sa.String(255),nullable=False),
                  sa.Column('is_admin', sa.Boolean,nullable=False),
                  sa.PrimaryKeyConstraint("id"),
                  sa.UniqueConstraint("email"))

def downgrade() -> None:
    op.drop_table("user")
