from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.features.ideas.schemas import IdeaIn, IdeaOut
from app.features.ideas.service import service
from app.db.session import get_db

router = APIRouter(prefix="/ideas", tags=["Ideas"])
service = service()
db_session = Annotated[Session, Depends(get_db)]


@router.post("", response_model=IdeaOut, status_code=201)
def create_idea(data:IdeaIn, db: db_session):
    return service.create_idea(db, data)

@router.get("/{id}", response_model=IdeaOut)
async def get_idea(db: db_session):
    raise service.get_idea(db=db, idea_id=id)