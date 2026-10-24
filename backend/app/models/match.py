from uuid import uuid4, UUID
from app.db.base import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String, Float, ForeignKey


class matches(Base):
#idea id
#match)id
    __tablename__ = "matches"
    idea_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("ideas.id"), primary_key=True)
    match_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("ideas.id"), primary_key=True)
    score: Mapped[Float] = mapped_column(float)
    domain_score: Mapped[Float] = mapped_column(float)
    skill_score: Mapped[Float] = mapped_column(float)
    explanation: Mapped[String] = mapped_column(String)