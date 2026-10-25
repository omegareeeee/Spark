from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.features.ideas.schemas import IdeaIn, IdeaOut, CommentOut, CommentIn
from app.features.ideas.service import service
from app.db.session import get_db

router = APIRouter(prefix="/ideas", tags=["Ideas"])
service = service()
db_session = Annotated[Session, Depends(get_db)]


@router.post("", response_model=IdeaOut, status_code=201)
def create_idea(data:IdeaIn, db: db_session):
    return service.create_idea(db, data)

@router.get("/{idea_id}", response_model=IdeaOut)
async def get_idea(idea_id: UUID, db: db_session):
    idea = service().get_idea(db, idea_id)
    if idea is None:
        raise HTTPException(status_code=404, detail="Idea not found")
    return idea

@router.get("", response_model=list[IdeaOut])
def get_all_ideas(db: db_session):
    return service.get_all_ideas(db)

@router.post("/{idea_id}/like")
def like_idea(idea_id: UUID, db: Session = Depends(get_db)):
    count = service.like_idea(db, idea_id)
    if count is None:
        raise HTTPException(404, "Idea not found")
    return {"like_count": count}