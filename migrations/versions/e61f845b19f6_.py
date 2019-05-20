"""empty message

Revision ID: e61f845b19f6
Revises: 8a2d105ea211
Create Date: 2019-05-20 10:26:36.511369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e61f845b19f6'
down_revision = '8a2d105ea211'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('category_restaurant_id_fkey', 'category', type_='foreignkey')
    op.create_foreign_key(None, 'category', 'user', ['user_id'], ['id'])
    op.drop_column('category', 'restaurant_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('restaurant_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'category', type_='foreignkey')
    op.create_foreign_key('category_restaurant_id_fkey', 'category', 'restaurant', ['restaurant_id'], ['id'])
    op.drop_column('category', 'user_id')
    # ### end Alembic commands ###
