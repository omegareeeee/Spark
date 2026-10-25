import uuid
from datetime import datetime
from pgvector.sqlalchemy import Vector
from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base

class Idea(Base):
    __tablename__ = "ideas"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    # person_id: Mapped[UUID] = mapped_column(ForeignKey("person.id", ondelete="CASCADE"),nullable=True)
    title: Mapped[str] = mapped_column(Text)
    description: Mapped[str] = mapped_column(Text)
    idea_embedding = mapped_column(Vector(384))
    github_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    x: Mapped[float | None]
    y: Mapped[float | None]
    cluster_id: Mapped[int | None] = mapped_column(ForeignKey("clusters.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # person: Mapped["Person"] = relationship(back_populates="ideas")