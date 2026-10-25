from datetime import datetime
from sqlalchemy import ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID
from app.db.base import Base

class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    idea_id: Mapped[UUID] = mapped_column(ForeignKey("ideas.id", ondelete="CASCADE"), index=True)
    author_name: Mapped[str] = mapped_column(String)
    text: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())