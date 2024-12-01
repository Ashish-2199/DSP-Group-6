"""Fix password_hash to be stored as BLOB

Revision ID: ede98b7391fa
Revises: 3e02f7a88853
Create Date: 2024-11-29 08:08:48.418605

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ede98b7391fa'
down_revision = '3e02f7a88853'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.LargeBinary(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.LargeBinary(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###