"""empty message

Revision ID: cee6b3578955
Revises: 5391a488bf50
Create Date: 2017-02-21 20:18:38.405835

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cee6b3578955'
down_revision = '5391a488bf50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=128), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True))
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
