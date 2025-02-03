"""Add rate_per_day  column to Car

Revision ID: f28f31d98552
Revises: ae181c7c380f
Create Date: 2025-02-03 14:24:38.996059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f28f31d98552'
down_revision: Union[str, None] = 'ae181c7c380f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('car', sa.Column('rate_per_day', sa.DECIMAL(precision=15, scale=2), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'car', type_='unique')
    op.drop_column('car', 'rate_per_day')
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
    sa.Column('status_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
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
    sa.Column('email', mysql.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'customer', ['id'], unique=True)
    op.create_index('email', 'customer', ['email'], unique=True)
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('first_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('dob', mysql.DATETIME(), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=100), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('customer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='user_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_index('id', 'user', ['id'], unique=True)
    op.create_index('email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
