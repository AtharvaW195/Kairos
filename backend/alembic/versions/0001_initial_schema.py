"""Create the initial Kairos schema."""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("email", sa.String(255), nullable=False), sa.Column("hashed_password", sa.String(255), nullable=False), sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False))
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_table("stocks", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("ticker", sa.String(16), nullable=False), sa.Column("name", sa.String(255), nullable=False), sa.Column("sector", sa.String(100), nullable=True))
    op.create_index("ix_stocks_ticker", "stocks", ["ticker"], unique=True)
    op.create_table("portfolio", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False), sa.Column("stock_id", sa.Integer(), sa.ForeignKey("stocks.id"), nullable=False), sa.Column("shares", sa.Float(), nullable=False), sa.Column("avg_price", sa.Float(), nullable=False), sa.UniqueConstraint("user_id", "stock_id", name="uq_portfolio_user_stock"))
    op.create_table("transactions", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False), sa.Column("stock_id", sa.Integer(), sa.ForeignKey("stocks.id"), nullable=False), sa.Column("type", sa.Enum("buy", "sell", name="transactiontype", native_enum=False), nullable=False), sa.Column("shares", sa.Float(), nullable=False), sa.Column("price", sa.Float(), nullable=False), sa.Column("timestamp", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False))
    op.create_table("watchlist", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id"), nullable=False), sa.Column("stock_id", sa.Integer(), sa.ForeignKey("stocks.id"), nullable=False), sa.Column("added_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False), sa.UniqueConstraint("user_id", "stock_id", name="uq_watchlist_user_stock"))


def downgrade() -> None:
    op.drop_table("watchlist")
    op.drop_table("transactions")
    op.drop_table("portfolio")
    op.drop_index("ix_stocks_ticker", table_name="stocks")
    op.drop_table("stocks")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
