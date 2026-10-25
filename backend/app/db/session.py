from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

url = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

def get_db():
    with SessionLocal() as session:
        yield session

# get_db()