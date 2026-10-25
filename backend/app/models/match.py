from uuid import uuid4, UUID
from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Float, ForeignKey


class Match(Base):
    __tablename__ = "matches"
    idea_id: Mapped[UUID] = mapped_column(ForeignKey("ideas.id",ondelete="CASCADE"), primary_key=True)
    match_id: Mapped[UUID] = mapped_column(ForeignKey("ideas.id",ondelete="CASCADE"), primary_key=True)
    score: Mapped[float]
    domain_score: Mapped[float | None]
    skill_score: Mapped[float | None]
    explanation: Mapped[str | None] = mapped_column(String)