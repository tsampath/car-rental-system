"""Add role_id column to user

Revision ID: f20f09c7127a
Revises: 
Create Date: 2025-02-02 11:02:55.506210

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f20f09c7127a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'role_id')
    op.create_table('car',
    sa.Column('car_id', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('make', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('model', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('year', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('mileage', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('availability', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.Column('minimum_rent_period', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('maximum_rent_period', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('booking',
    sa.Column('car_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('customer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('booking_start_date', mysql.DATETIME(), nullable=False),
    sa.Column('booking_end_date', mysql.DATETIME(), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('is_closed', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('closed_date', mysql.DATETIME(), nullable=True),
    sa.Column('additional_comment', mysql.VARCHAR(length=1000), nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['car_id'], ['car.id'], name='booking_ibfk_1', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='booking_ibfk_2', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'booking', ['id'], unique=True)
    op.create_table('customer',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('building_name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('address_line_1', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('address_line_2', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('town', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('customer_type_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('price_list_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'customer', ['id'], unique=True)
    # ### end Alembic commands ###
