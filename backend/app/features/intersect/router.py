from fastapi import APIRouter, HTTPException, Depends

from typing import Annotated

from app.features.intersect.service import service
from app.features.intersect.schemas import IntersectOut, Bridge, IntersectIn

from app.db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/intersection", tags=["intersections"])
service = service()
db_session = Annotated[Session, Depends(get_db)]

@router.get("",response_model=list[Bridge])
def get_interection(db: db_session, setlimit: int = 5):
    return [
        {"a": p["a"], "b": p["b"], "similarity": p["similarity"]}
        for p in service.find_bridges(db, limit=setlimit)
    ]


@router.post("", response_model=IntersectOut)
def intersect(db: db_session, data: IntersectIn):
    result = service.combine(db, data.idea_a_id, data.idea_b_id)
    if result == "not_found":
        raise HTTPException(404, "Idea not found")
    if result is None:
        raise HTTPException(503, "Could not generate a combined idea, try again")
    return result