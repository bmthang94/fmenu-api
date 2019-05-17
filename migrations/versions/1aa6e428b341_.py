"""empty message

Revision ID: 1aa6e428b341
Revises: 6e9c0f5b5824
Create Date: 2019-05-15 09:42:08.338276

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '1aa6e428b341'
down_revision = '6e9c0f5b5824'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('flask_dance_oauth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('token', sqlalchemy_utils.types.json.JSONType(), nullable=False),
    sa.Column('provider_user_id', sa.String(length=256), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('provider_user_id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.add_column('order', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'order', 'user', ['user_id'], ['id'])
    op.drop_constraint('user_firstname_key', 'user', type_='unique')
    op.drop_constraint('user_lastname_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_lastname_key', 'user', ['lastname'])
    op.create_unique_constraint('user_firstname_key', 'user', ['firstname'])
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.drop_column('order', 'user_id')
    op.drop_table('token')
    op.drop_table('flask_dance_oauth')
    # ### end Alembic commands ###