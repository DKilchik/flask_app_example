"""correct answer field added 

Revision ID: e908f768f5ba
Revises: 97f8f44d4ed1
Create Date: 2020-06-10 15:52:18.319301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e908f768f5ba'
down_revision = '97f8f44d4ed1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('correct_ans', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('questions', 'correct_ans')
    # ### end Alembic commands ###
