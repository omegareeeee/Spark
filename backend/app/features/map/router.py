from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.features.ideas.schemas import IdeaIn, IdeaOut
from app.features.ideas.service import service
from app.db.session import get_db

router = APIRouter()

db_session = Annotated[Session, Depends(get_db)]

# @router.get()
# def getMap():
#     pass //TODO 