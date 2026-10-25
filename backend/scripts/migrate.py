import sys
from sqlalchemy import event, DDL

from app.db.base import Base
from app.db.session import engine
import app.models  # noqa: F401  (registers all tables)

if "--reset" in sys.argv:
    Base.metadata.drop_all(engine)
    print("Dropped all tables")


event.listen(
    Base.metadata,
    "before_create",
    DDL("CREATE EXTENSION IF NOT EXISTS vector;")
)

Base.metadata.create_all(engine)
print("Tables created:", ", ".join(Base.metadata.tables))