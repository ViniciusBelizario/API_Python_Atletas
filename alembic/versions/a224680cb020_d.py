"""$(d)

Revision ID: a224680cb020
Revises: fed90fff1004
Create Date: 2024-05-20 20:43:08.299522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a224680cb020'
down_revision: Union[str, None] = 'fed90fff1004'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('atletas', sa.Column('categoria_id', sa.Integer(), nullable=False))
    op.drop_constraint('atletas_catergoria_id_fkey', 'atletas', type_='foreignkey')
    op.create_foreign_key(None, 'atletas', 'categorias', ['categoria_id'], ['pk_id'])
    op.drop_column('atletas', 'catergoria_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('atletas', sa.Column('catergoria_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'atletas', type_='foreignkey')
    op.create_foreign_key('atletas_catergoria_id_fkey', 'atletas', 'categorias', ['catergoria_id'], ['pk_id'])
    op.drop_column('atletas', 'categoria_id')
    # ### end Alembic commands ###