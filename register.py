from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session# Adjust the import path according to your project structure
from schemas.reg import UserCreate ,UserUpdate ,UserLogin  # Adjust the import path
import bcrypt
from passlib.context import CryptContext
from model.reg import users
# Adjust the import path
from database import SessionLocal, engine

from fastapi import APIRouter

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Helper function to verify password
def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@router.post("/register")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Convert Pydantic model to dict and insert into the database using SQLAlchemy
    # Assuming 'user' is your Pydantic model
    hashed_password = hash_password(user.password)  # Replace with your actual password hashing method
    user_data = user.dict()
    user_data['password'] = hashed_password
    query = users.insert().values(**user_data)
    result = db.execute(query)
    db.commit()  # Commit the transaction
    return {"id": result.inserted_primary_key[0]}

@router.post("/login")
async def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    # Retrieve user from the database
    user = db.query(users).filter(users.c.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # Verify password (ensure passwords are hashed in your database)
    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # Include the branchId in the response
    id = user.id  # Replace 'user.branch_id' with the actual way to get branchId from the user record
    return {
        "message": "Login successful for user: {}".format(user.email),
        "userID": id
    }


