from sqlalchemy import text
from app.db.base import Base
from app.db.session import engine
import app.models  # noqa: F401  (registers all tables)

with engine.begin() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

Base.metadata.create_all(engine)
print("Tables created:", ", ".join(Base.metadata.tables))

import sys
if "--reset" in sys.argv:
    Base.metadata.drop_all(engine)
    print("Dropped all tables")