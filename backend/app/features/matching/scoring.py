from sklearn.metrics.pairwise import cosine_similarity
from app.core.config import SIM_CENTER, SIM_WIDTH
import math


def score_pair(a: dict, b: dict) -> dict:
    sim = cosine_similarity(a["idea_emb"], b["idea_emb"])
    score = math.exp(-0.5 * ((sim - SIM_CENTER) / SIM_WIDTH) ** 2)
    return {"score": score, "similarity": sim}

def rank(me, others, k):
    scored = [(o, score_pair(me, o)) for o in others if o["id"] != me["id"]]
    scored.sort(key=lambda t: t[1]["score"], reverse=True)
    return scored[:k]