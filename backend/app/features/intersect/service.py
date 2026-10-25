

import numpy as np
from uuid import UUID
from sqlalchemy.orm import Session

from app.core.llm import explain_intersection
from app.models import Idea

_cache: dict[tuple, dict] = {}   # demo answers stay instant after the first call

class service():
    def find_bridges(self, db: Session, limit: int = 5, min_similarity: float = 0.3) -> list[dict]:
        """Pairs of ideas in DIFFERENT clusters whose meaning is closest."""
        ideas = (
            db.query(Idea)
            .filter(Idea.idea_embedding.isnot(None), Idea.cluster_id.isnot(None))
            .all()
        )
        if len(ideas) < 2:
            return []

        X = np.array([np.asarray(i.idea_embedding, dtype=np.float32) for i in ideas])
        X /= np.linalg.norm(X, axis=1, keepdims=True) + 1e-9   # length 1, so dot product = cosine
        sims = X @ X.T

        pairs = []
        for i in range(len(ideas)):
            for j in range(i + 1, len(ideas)):
                if ideas[i].cluster_id != ideas[j].cluster_id and sims[i, j] >= min_similarity:
                    pairs.append((float(sims[i, j]), ideas[i], ideas[j]))

        pairs.sort(key=lambda p: p[0], reverse=True)
        return [{"a": a, "b": b, "similarity": round(s, 3)} for s, a, b in pairs[:limit]]


    def combine(self, db: Session, id_a: UUID, id_b: UUID) -> dict | None | str:
        """Returns the result dict, "not_found", or None if the LLM failed."""
        a, b = db.get(Idea, id_a), db.get(Idea, id_b)
        if a is None or b is None:
            return "not_found"

        key = tuple(sorted((str(id_a), str(id_b))))
        if key not in _cache:
            out = explain_intersection(
                {"title": a.title, "description": a.description},
                {"title": b.title, "description": b.description},
            )
            if out is None:
                return None
            _cache[key] = out
        return {"a": a, "b": b, **_cache[key]}