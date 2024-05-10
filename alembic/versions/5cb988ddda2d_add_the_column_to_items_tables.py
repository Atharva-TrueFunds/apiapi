"""Add the column to items tables

Revision ID: 5cb988ddda2d
Revises: e9ccf961d3ae
Create Date: 2024-05-10 15:50:34.273794

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5cb988ddda2d"
down_revision: Union[str, None] = "e9ccf961d3ae"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("items", sa.Column("color", sa.String(50)))


def downgrade() -> None:
    op.drop_column("items", "color")
