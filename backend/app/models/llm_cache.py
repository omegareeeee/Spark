from datetime import datetime
from sqlalchemy import Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class LLMCache(Base):
    __tablename__ = "llm_cache"

    key: Mapped[str] = mapped_column(Text, primary_key=True)
    response: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())