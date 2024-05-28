"""Add difficulty_id to use_case

Revision ID: df47a9194953
Revises:
Create Date: 2024-05-25 20:48:51.825006

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "df47a9194953"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("use_cases")
    op.drop_table("risk_factor_matrix")
    op.drop_table("learning_paths")
    op.drop_table("difficulty_level")
    op.drop_table("lesson")
    op.drop_table("users")
    op.drop_table("user_answers")
    op.drop_table("questions")
    op.drop_table("options")
    op.drop_table("lessons")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "lessons",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", sa.TEXT(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="lessons_pkey"),
    )
    op.create_table(
        "options",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('options_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("question_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("is_correct", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["questions.id"],
            name="options_question_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="options_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "questions",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('questions_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("use_case_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("text", sa.TEXT(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["use_case_id"],
            ["use_cases.id"],
            name="questions_use_case_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="questions_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "user_answers",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("use_case_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("question_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("option_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("is_correct", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            autoincrement=False,
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["option_id"],
            ["options.id"],
            name="user_answers_option_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["question_id"],
            ["questions.id"],
            name="user_answers_question_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["use_case_id"],
            ["use_cases.id"],
            name="user_answers_use_case_id_fkey",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="user_answers_user_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="user_answers_pkey"),
    )
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('users_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "username", sa.VARCHAR(length=255), autoincrement=False, nullable=True
        ),
        sa.Column("email", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column(
            "hashed_password",
            sa.VARCHAR(length=255),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "use_case_difficulty", sa.VARCHAR(), autoincrement=False, nullable=True
        ),
        sa.Column(
            "score",
            sa.DOUBLE_PRECISION(precision=53),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "is_admin",
            sa.BOOLEAN(),
            server_default=sa.text("false"),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.UniqueConstraint("email", name="users_email_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "lesson",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="lesson_pkey"),
    )
    op.create_table(
        "difficulty_level",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('difficulty_level_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("level", sa.VARCHAR(length=50), autoincrement=False, nullable=False),
        sa.PrimaryKeyConstraint("id", name="difficulty_level_pkey"),
        sa.UniqueConstraint("level", name="difficulty_level_level_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_table(
        "learning_paths",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("name", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="learning_paths_pkey"),
    )
    op.create_table(
        "risk_factor_matrix",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("factor", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("score", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("use_case_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["use_case_id"],
            ["use_cases.id"],
            name="risk_factor_matrix_use_case_id_fkey",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="risk_factor_matrix_pkey"),
    )
    op.create_table(
        "use_cases",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("description", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("type", sa.VARCHAR(length=255), autoincrement=False, nullable=True),
        sa.Column("difficulty_name", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("multiple_risks", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("final_decision", sa.TEXT(), autoincrement=False, nullable=True),
        sa.Column("lesson_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("created_by_user", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column(
            "risk_factors",
            postgresql.JSONB(astext_type=sa.Text()),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("difficulty_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["created_by_user"], ["users.id"], name="fk_created_by_user"
        ),
        sa.ForeignKeyConstraint(
            ["difficulty_id"], ["difficulty_level.id"], name="fk_difficulty"
        ),
        sa.PrimaryKeyConstraint("id", name="use_cases_pkey"),
    )
    # ### end Alembic commands ###