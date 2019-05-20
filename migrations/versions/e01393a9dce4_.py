"""empty message

Revision ID: e01393a9dce4
Revises: e61f845b19f6
Create Date: 2019-05-20 11:14:16.652271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e01393a9dce4'
down_revision = 'e61f845b19f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('status', sa.Integer(), nullable=True))
    op.add_column('dish', sa.Column('status', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'status')
    op.drop_column('dish', 'status')
    op.drop_column('category', 'status')
    # ### end Alembic commands ###
