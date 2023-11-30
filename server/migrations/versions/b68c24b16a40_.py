"""empty message

Revision ID: b68c24b16a40
Revises: 721bd2a98059
Create Date: 2023-11-30 11:51:05.921427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b68c24b16a40'
down_revision = '721bd2a98059'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.add_column(sa.Column('google_client_id', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('google_client_secret', sa.String(length=200), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('admin', schema=None) as batch_op:
        batch_op.drop_column('google_client_secret')
        batch_op.drop_column('google_client_id')

    # ### end Alembic commands ###