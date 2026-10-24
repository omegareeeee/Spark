from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import DATABASE_URL

url = DATABASE_URL.replace("postgresql://", "postgresql+psycopg://", 1)

engine = create_engine(url, pool_size=5, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False)

def get_db():
    with SessionLocal() as session:
        yield session