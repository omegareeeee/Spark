# from uuid import UUID, uuid4
# from datetime import datetime
# from sqlalchemy import String, DateTime, func
# from sqlalchemy.orm import relationship, Mapped,mapped_column
# from sqlalchemy.dialects.postgresql import ARRAY
# from app.db.base import Base

# from sqlalchemy.orm import Mapped, mapped_column

# class Person(Base):
#     __tablename__ = "person"
    
#     id: Mapped[UUID] = mapped_column(
#         primary_key= True,
#         default=uuid4,
#     )

#     name: Mapped[str] = mapped_column(String)

#     handle: Mapped[str] = mapped_column(
#         nullable=False,
#     )

#     skills_have: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)
#     skills_need: Mapped[list[str]] = mapped_column(ARRAY(String), default=list)

#     created_at: Mapped[datetime] = mapped_column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         nullable=False,
#     )

#     ideas: Mapped[list["Idea"]] = relationship(
#         back_populates="person", cascade="all, delete"
#     )

