import uuid
from datetime import datetime
from pgvector.sqlalchemy import Vector
from sqlalchemy import ForeignKey, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.config import EMBED_DIM
from app.db.base import Base

class Idea(Base):
    __tablename__ = "ideas"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    person_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("people.id", ondelete="CASCADE"))
    text: Mapped[str] = mapped_column(Text)
    idea_embedding = mapped_column(Vector(EMBED_DIM))
    have_embedding = mapped_column(Vector(EMBED_DIM))
    need_embedding = mapped_column(Vector(EMBED_DIM))
    x: Mapped[float | None]
    y: Mapped[float | None]
    cluster_id: Mapped[int | None] = mapped_column(ForeignKey("clusters.id"))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    person: Mapped["Person"] = relationship(back_populates="ideas")