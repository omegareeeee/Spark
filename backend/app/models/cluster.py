from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Cluster(Base):
    __tablename__ = "clusters"

    id: Mapped[Integer] = mapped_column(primary_key=True, autoincrement=False)
    label: Mapped[String] = mapped_column(String)