from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.features.cluster.service import rebuild_clusters
from app.models import Idea, Cluster

router = APIRouter(prefix="/clusters", tags=["clusters"])


@router.get("")
def list_clusters(db: Session = Depends(get_db)):
    out = []
    for c in db.query(Cluster).all():
        ideas = db.query(Idea).filter(Idea.cluster_id == c.id).all()
        out.append({
            "id": c.id,
            "cluster": c.label,
            "ideas": [{"id": str(i.id), "title": i.title, "author_name": i.author_name}
                      for i in ideas],
        })
    return out


@router.post("/rebuild")
def rebuild(db: Session = Depends(get_db)):
    return {"clusters": rebuild_clusters(db)}