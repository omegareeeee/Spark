import numpy as np
from sklearn.cluster import KMeans
from sqlalchemy.orm import Session

from app.core.llm import name_cluster
from app.features.map import layout
from app.models import Idea, Cluster

MIN_IDEAS = 10   # UMAP and KMeans behave badly below this


def rebuild_clusters(db: Session) -> int:
    """Re-lay out the map and regroup ALL ideas from scratch."""
    ideas = db.query(Idea).filter(Idea.idea_embedding.isnot(None)).all()
    if len(ideas) < MIN_IDEAS:
        return 0

    X = np.array([np.asarray(i.idea_embedding, dtype=np.float32) for i in ideas])

    # 1. Map positions (also saves umap_model.pkl)
    coords = layout.fit(X)
    for idea, (x, y) in zip(ideas, coords):
        idea.x, idea.y = float(x), float(y)

    # 2. Groups: about 4 ideas each, between 2 and 6 groups
    k = max(2, min(6, len(ideas) // 4))
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(X)

    # 3. Clear old groups (detach ideas first, because of the foreign key)
    db.query(Idea).update({Idea.cluster_id: None})
    db.query(Cluster).delete()
    db.flush()

    # 4. Save each group, name it, attach its ideas
    for c in range(k):
        members = [idea for idea, lab in zip(ideas, km.labels_) if lab == c]
        name = name_cluster(
            [{"title": m.title, "description": m.description} for m in members]
        ) or f"Group {c + 1}"
        cluster = Cluster(label=name, center=km.cluster_centers_[c].tolist())
        db.add(cluster)
        db.flush()   # gives the cluster its id
        for m in members:
            m.cluster_id = cluster.id

    db.commit()
    return k


def assign_cluster(db: Session, embedding) -> int | None:
    """Put ONE new idea into the closest existing group. Returns None if no groups yet."""
    clusters = db.query(Cluster).all()
    if not clusters:
        return None
    vec = np.asarray(embedding, dtype=np.float32)
    closest = min(
        clusters,
        key=lambda c: np.linalg.norm(np.asarray(c.center, dtype=np.float32) - vec),
    )
    return closest.id