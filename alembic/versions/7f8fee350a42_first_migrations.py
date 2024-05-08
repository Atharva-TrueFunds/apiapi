"""First Migrations

Revision ID: 7f8fee350a42
Revises: c8b853d9f387
Create Date: 2024-05-08 16:13:20.321477

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f8fee350a42'
down_revision: Union[str, None] = 'c8b853d9f387'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
