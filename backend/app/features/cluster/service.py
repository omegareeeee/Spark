import numpy as np
from sklearn.cluster import KMeans
from sqlalchemy.orm import Session
from app.core.llm import name_cluster
from app.models import Idea, Cluster

MIN_IDEAS=5
class service():

    def rebuild_clusters(db: Session):
        ideas = db.query(Idea).filter(Idea.idea_embedding.isnot(None)).all()

        if len(ideas) < 5:
            return 0

        embedding = np.array([i.idea_embedding for i in ideas])

        k = max(2, min(6, len(ideas) // 4))

        km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(embedding)
        db.query(Idea).update({Idea.cluster_id: None})
        db.query(Cluster).delete()
        db.flush()

        for c in range(k):
            members = [idea for idea, label in zip(ideas, km.labels_) if label == c]
            name = name_cluster([m.title for m in members]) or f"Group {c + 1}"

        db.commit()
        return k
            

    # def addIdeaToCluster():