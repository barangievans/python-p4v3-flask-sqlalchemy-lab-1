"""initial migration

Revision ID: 2676ca00bec1
Revises: ecd021f54f92
Create Date: 2024-10-02 22:48:56.896989

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2676ca00bec1'
down_revision = 'ecd021f54f92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('earthquakes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('earthquakes',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('magnitude', sa.FLOAT(), nullable=True),
    sa.Column('location', sa.VARCHAR(), nullable=True),
    sa.Column('year', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
