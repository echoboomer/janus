"""Adjust relationships for incidents table

Revision ID: a356e9f16eef
Revises: e8a0a978b5f7
Create Date: 2024-12-28 15:07:20.188012

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "a356e9f16eef"
down_revision = "e8a0a978b5f7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "incidentevent_parent_fkey", "incidentevent", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "incidentevent",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "incidentparticipant_parent_fkey",
        "incidentparticipant",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "incidentparticipant",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "jiraissuerecord_parent_fkey", "jiraissuerecord", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "jiraissuerecord",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "opsgenieincidentrecord_parent_fkey",
        "opsgenieincidentrecord",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "opsgenieincidentrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "pagerdutyincidentrecord_parent_fkey",
        "pagerdutyincidentrecord",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "pagerdutyincidentrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "postmortemrecord_parent_fkey", "postmortemrecord", type_="foreignkey"
    )
    op.create_foreign_key(
        None,
        "postmortemrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "statuspageincidentrecord_parent_fkey",
        "statuspageincidentrecord",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None,
        "statuspageincidentrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "statuspageincidentrecord", type_="foreignkey")
    op.create_foreign_key(
        "statuspageincidentrecord_parent_fkey",
        "statuspageincidentrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    op.drop_constraint(None, "postmortemrecord", type_="foreignkey")
    op.create_foreign_key(
        "postmortemrecord_parent_fkey",
        "postmortemrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    op.drop_constraint(None, "pagerdutyincidentrecord", type_="foreignkey")
    op.create_foreign_key(
        "pagerdutyincidentrecord_parent_fkey",
        "pagerdutyincidentrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    op.drop_constraint(None, "opsgenieincidentrecord", type_="foreignkey")
    op.create_foreign_key(
        "opsgenieincidentrecord_parent_fkey",
        "opsgenieincidentrecord",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    op.drop_constraint(None, "jiraissuerecord", type_="foreignkey")
    op.create_foreign_key(
        "jiraissuerecord_parent_fkey",
        "jiraissuerecord",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    op.drop_constraint(None, "incidentparticipant", type_="foreignkey")
    op.create_foreign_key(
        "incidentparticipant_parent_fkey",
        "incidentparticipant",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    op.drop_constraint(None, "incidentevent", type_="foreignkey")
    op.create_foreign_key(
        "incidentevent_parent_fkey",
        "incidentevent",
        "incidentrecord",
        ["parent"],
        ["id"],
    )
    # ### end Alembic commands ###