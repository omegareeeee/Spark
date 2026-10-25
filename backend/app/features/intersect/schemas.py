import uuid
from pydantic import BaseModel, model_validator


class Ideas(BaseModel):
    id: uuid.UUID
    title: str
    author_name: str
    cluster_id: int | None = None


class Bridge(BaseModel):
    a: Ideas
    b: Ideas
    similarity: float


class IntersectIn(BaseModel):
    idea_a_id: uuid.UUID
    idea_b_id: uuid.UUID

    @model_validator(mode="after")
    def different(self):
        if self.idea_a_id == self.idea_b_id:
            raise ValueError("pick two different ideas")
        return self


class IntersectOut(BaseModel):
    a: Ideas
    b: Ideas
    title: str
    pitch: str
    why: str