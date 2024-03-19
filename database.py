# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# # Your MySQL connection string
# DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost:3306/assistant"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Your Azure MySQL connection details
username = "monasha"
password = "error404@PHP"
server_name = "dbassistance.mysql.database.azure.com"
database_name = "assistant"

DATABASE_URL = f"mysql+mysqlconnector://{username}@{server_name}/{database_name}?password={password}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


