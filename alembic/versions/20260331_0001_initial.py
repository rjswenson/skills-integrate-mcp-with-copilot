"""initial activities and registrations tables

Revision ID: 20260331_0001
Revises:
Create Date: 2026-03-31 00:00:00
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20260331_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "activities",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("schedule", sa.String(), nullable=False),
        sa.Column("max_participants", sa.Integer(), nullable=False),
    )
    op.create_index("ix_activities_id", "activities", ["id"], unique=False)
    op.create_index("ix_activities_name", "activities", ["name"], unique=True)

    op.create_table(
        "registrations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("activity_id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(["activity_id"], ["activities.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("activity_id", "email", name="uq_activity_email"),
    )
    op.create_index("ix_registrations_id", "registrations", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_registrations_id", table_name="registrations")
    op.drop_table("registrations")

    op.drop_index("ix_activities_name", table_name="activities")
    op.drop_index("ix_activities_id", table_name="activities")
    op.drop_table("activities")
