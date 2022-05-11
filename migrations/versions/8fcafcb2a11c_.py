"""empty message

Revision ID: 8fcafcb2a11c
Revises: 12fe4a3542c4
Create Date: 2022-05-11 13:57:01.725929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fcafcb2a11c'
down_revision = '12fe4a3542c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=255), nullable=True),
    sa.Column('product_price', sa.Integer(), nullable=True),
    sa.Column('product_desc', sa.String(length=255), nullable=True),
    sa.Column('product_img_path', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###