from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.idea import Idea
from app.models.comment import Comment

from app.features.comments.schemas import CommentIn, CommentOut
from app.db.session import get_db

router = APIRouter(prefix="/ideas", tags=["Comments"])
db_session = Annotated[Session, Depends(get_db)]


@router.get("/{idea_id}/comments", response_model=list[CommentOut])
def list_comments(idea_id: UUID, db: Session = Depends(get_db)):
    if not db.get(Idea, idea_id):
        raise HTTPException(404, "Idea not found")
    return (
        db.query(Comment)
        .filter(Comment.idea_id == idea_id)
        .order_by(Comment.created_at)      # oldest first, like a thread
        .all()
    )

@router.post("/{idea_id}/comments", response_model=CommentOut,)
def add_comments(idea_id: UUID, data: CommentIn, db:db_session):

    if not db.get(Idea, idea_id):
        raise HTTPException(404, "Idea not found")

    comment = Comment(
        idea_id = idea_id,
        author_name = data.author_name.strip(),
        text = data.text.strip(),
    )

    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

