"""Initial commit

Revision ID: c1d6d526637a
Revises: 
Create Date: 2024-09-16 10:29:49.897853

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = "c1d6d526637a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "applicationdata",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("data", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("deletable", sa.Boolean(), nullable=True),
        sa.Column(
            "description", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("json_data", sa.JSON(), nullable=True),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "incidentrecord",
        sa.Column("additional_comms_channel", sa.Boolean(), nullable=True),
        sa.Column(
            "additional_comms_channel_id",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True,
        ),
        sa.Column(
            "additional_comms_channel_link",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True,
        ),
        sa.Column(
            "boilerplate_message_ts",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True,
        ),
        sa.Column(
            "channel_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "channel_name", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "components", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "description", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "digest_message_ts",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=True,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("impact", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("is_security_incident", sa.Boolean(), nullable=True),
        sa.Column("last_update_sent", sa.DateTime(), nullable=True),
        sa.Column("link", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column(
            "meeting_link", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("roles", sa.JSON(), nullable=True),
        sa.Column("roles_all", sa.JSON(), nullable=True),
        sa.Column(
            "severity", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("severities", sa.JSON(), nullable=True),
        sa.Column("slug", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("statuses", sa.JSON(), nullable=True),
        sa.Column("tags", sa.JSON(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "maintenancewindowrecord",
        sa.Column("channels", sa.JSON(), nullable=True),
        sa.Column("components", sa.JSON(), nullable=True),
        sa.Column(
            "contact", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "description", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("end_timestamp", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("start_timestamp", sa.DateTime(), nullable=True),
        sa.Column(
            "status", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column(
            "email",
            sqlmodel.sql.sqltypes.AutoString(length=255),
            nullable=False,
        ),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column(
            "full_name",
            sqlmodel.sql.sqltypes.AutoString(length=255),
            nullable=True,
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "hashed_password",
            sqlmodel.sql.sqltypes.AutoString(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=True)
    op.create_table(
        "incidentevent",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("image", sa.LargeBinary(), nullable=True),
        sa.Column(
            "incident_slug", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "message_ts", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column(
            "mimetype", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.Column(
            "source", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column("text", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=True),
        sa.Column("title", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("user", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "incidentparticipant",
        sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("is_lead", sa.Boolean(), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.Column("role", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column(
            "user_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.Column(
            "user_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "jiraissuerecord",
        sa.Column("key", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("team", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("url", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("key"),
    )
    op.create_table(
        "opsgenieincidentrecord",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pagerdutyincidentrecord",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "postmortemrecord",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.Column("url", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "statuspageincidentrecord",
        sa.Column(
            "channel_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column(
            "message_ts", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("parent", sa.Integer(), nullable=False),
        sa.Column(
            "shortlink", sqlmodel.sql.sqltypes.AutoString(), nullable=True
        ),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("updates", sa.JSON(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent"],
            ["incidentrecord.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("statuspageincidentrecord")
    op.drop_table("postmortemrecord")
    op.drop_table("pagerdutyincidentrecord")
    op.drop_table("opsgenieincidentrecord")
    op.drop_table("jiraissuerecord")
    op.drop_table("incidentparticipant")
    op.drop_table("incidentevent")
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    op.drop_table("maintenancewindowrecord")
    op.drop_table("incidentrecord")
    op.drop_table("applicationdata")
    # ### end Alembic commands ###