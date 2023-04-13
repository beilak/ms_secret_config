from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
)

metadata = MetaData()

user_table = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_name", String),
    Column("first_name", String),
    Column("last_name", String),
    Column("email", String),
    Column("phone", String),
)