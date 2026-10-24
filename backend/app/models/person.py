from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.dialects.postgresql import ARRAY
from app.db.base import Base

from sqlalchemy.orm import Mapped, mapped_column

class Person(Base):
    id: Mapped[UUID] = mapped_column(
        primary_key= True,
        default=uuid4,
    )

    username: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        nullable=False,
    )

    handle: Mapped[str] = mapped_column(
        String(16),
        unique=True,
        nullable=False,
    )

    skill_have: Mapped[str] = mapped_column(ARRAY(String))

    skill_needed: Mapped[str] = mapped_column(ARRAY(String))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

