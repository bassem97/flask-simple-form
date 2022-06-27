"""replace description with url

Revision ID: 529f957f2f83
Revises: 
Create Date: 2022-06-05 23:53:14.421540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '529f957f2f83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_site_title'), 'site', ['title'], unique=False)
    op.create_index(op.f('ix_site_url'), 'site', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_site_url'), table_name='site')
    op.drop_index(op.f('ix_site_title'), table_name='site')
    op.drop_table('site')
    # ### end Alembic commands ###
