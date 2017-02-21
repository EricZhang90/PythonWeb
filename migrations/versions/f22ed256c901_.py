"""empty message

Revision ID: f22ed256c901
Revises: cee6b3578955
Create Date: 2017-02-21 20:20:28.169105

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f22ed256c901'
down_revision = 'cee6b3578955'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
