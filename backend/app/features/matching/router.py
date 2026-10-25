from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.features.matching import service

router = APIRouter()

@router.get("/{idea_id}")
def matches(idea_id: str, db: Session = Depends(get_db)):
    result = service.get_matches(db, idea_id)

    if result is None:
        raise HTTPException(404, "idea not found")
    
    return result