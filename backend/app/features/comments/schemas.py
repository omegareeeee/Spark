from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class CommentIn(BaseModel):
    author_name: str = Field(min_length=1, max_length=80)
    text: str = Field(min_length=1, max_length=1000)

class CommentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # lets it read DB objects directly

    id: int
    idea_id: int
    author_name: str
    text: str
    created_at: datetime