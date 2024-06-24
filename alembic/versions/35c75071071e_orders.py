"""orders

Revision ID: 35c75071071e
Revises: 310251e91f1f
Create Date: 2024-06-20 21:37:19.875805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35c75071071e'
down_revision: Union[str, None] = '310251e91f1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('order',
                  sa.Column('id',sa.Integer,nullable=False),
                  sa.Column('customer_name', sa.String(100),nullable=False),
                  sa.Column('items_order',sa.String(60),nullable=False),
                  sa.Column('order_id',sa.Integer(),nullable=False),
                  sa.Column('total_price', sa.Float(),nullable=False),
                  sa.Column('customer_id', sa.Integer(),nullable=False),
                  sa.Column('menu_id', sa.String(50),nullable=False),
                  sa.Column('quantity', sa.String(50),nullable=False),
                  sa.PrimaryKeyConstraint("id"),
                  sa.ForeignKeyConstraint(["customer_id"],["user.id"],name="order_id_fkey",
            ondelete="CASCADE",
            onupdate="CASCADE"
        ),
        
)
                    
    

def downgrade() -> None:
    op.drop_table('order')
