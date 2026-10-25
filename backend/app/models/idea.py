import uuid
from datetime import datetime
from pgvector.sqlalchemy import Vector
from sqlalchemy import ForeignKey, Text, func, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship, column_property
from app.db.base import Base
from app.models.comment import Comment

class Idea(Base):
    __tablename__ = "ideas"

    author_name: Mapped[str] = mapped_column(Text)
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    idea_embedding = mapped_column(Vector(384))
    github_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    x: Mapped[float | None]
    y: Mapped[float | None]
    cluster_id: Mapped[int | None] = mapped_column(ForeignKey("clusters.id"), nullable=True)
    like_count: Mapped[int] = mapped_column(default=0, server_default="0")
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    comment_count: Mapped[int] = column_property(
        select(func.count(Comment.id))
        .where(Comment.idea_id == id)
        .correlate_except(Comment)
        .scalar_subquery()
    )

  