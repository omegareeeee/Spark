import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class IdeaIn(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    description: str = Field(min_length=10, max_length=1500)
    github_url: str | None = None
    contact: str = Field(min_length=1, max_length=120)
    author_name: str = Field(min_length=1, max_length=80)

class CommentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    author_name: str
    text: str
    created_at: datetime

class IdeaOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    # person_id: uuid.UUID
    description: str
    github_url: str | None = None
    x: float | None = None
    y: float | None = None
    cluster_id: int | None = None
    created_at: datetime