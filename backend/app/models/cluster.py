from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class Cluster(Base):
    __tablename__ = "clusters"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    label: Mapped[str] = mapped_column(String)
    center: Mapped[list] = mapped_column(JSON)