import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator
from uuid import UUID


class IdeaIn(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=10, max_length=1500)
    github_url: str | None = None
    contact: str = Field(min_length=1, max_length=120)
    author_name: str = Field(min_length=1, max_length=80)

class IdeaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str
    author_name: str
    github_url: str | None = None
    x: float | None = None
    y: float | None = None
    cluster_id: int | None = None
    created_at: datetime
    comment_count: int = 0

class CommentIn(BaseModel):
    author_name: str = Field(min_length=1, max_length=80)
    text: str = Field(min_length=1, max_length=1000)
    ideaId: UUID


class CommentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    author_name: str
    text: str
    like: int
    created_at: datetime