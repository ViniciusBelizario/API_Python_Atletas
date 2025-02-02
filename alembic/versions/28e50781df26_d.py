"""$(d)

Revision ID: 28e50781df26
Revises: 598722b2f43b
Create Date: 2024-05-21 00:33:38.389521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28e50781df26'
down_revision: Union[str, None] = '598722b2f43b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('centros_treinamento', sa.Column('proprietario', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('centros_treinamento', 'proprietario')
    # ### end Alembic commands ###
