from sqlalchemy import MetaData, Table, Column, Integer, String, Float, ForeignKey, Text

metadata = MetaData()


users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(255), unique=True),
    Column("password", String(255)),
    
)
