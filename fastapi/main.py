
# Schemas
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker

SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Database Setup
DATABASE_URL = "mariadb+mariadbconnector://root:12345@localhost:3306/pytest"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    db = SessionLocal()
    result = db.execute(text("SELECT 1"))
    print("Session 연결 성공:",result.fetchone())
finally:
    db.close()