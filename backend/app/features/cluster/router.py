from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models import Idea, Cluster
# from app.features.clusters.service import rebuild_clusters

router = APIRouter()

@router.get("/")
def list_clusters(db: Session = Depends(get_db)):
    out = []
    for c in db.query(Cluster).all():
        ideas = db.query(Idea).filter(Idea.cluster_id == c.id).all()
        out.append({
            "id": c.id,
            "cluster": c.label,
            "ideas": [{"id": i.id, "title": i.title, "author_name": i.author_name}
                      for i in ideas],
        })
    return out

# @router.post("/rebuild")
# def rebuild(db: Session = Depends(get_db)):
#     return {"clusters": rebuild_clusters(db)}