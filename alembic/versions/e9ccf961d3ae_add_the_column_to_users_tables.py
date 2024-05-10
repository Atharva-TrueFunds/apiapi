"""Add the column to users tables

Revision ID: e9ccf961d3ae
Revises: 
Create Date: 2024-05-10 15:50:27.240243

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e9ccf961d3ae"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users", sa.Column("city", sa.String(50)))


def downgrade() -> None:
    op.drop_column("users", "city")
