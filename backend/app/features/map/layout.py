from pathlib import Path

import joblib
import numpy as np
import umap

# app/features/map/layout.py -> parents[2] is app/
MODEL_PATH = Path(__file__).resolve().parents[2] / "artifacts" / "umap_model.pkl"
_reducer = None 


def fit(embeddings) -> np.ndarray:
    """Run ONCE on all ideas. Returns an (n, 2) array of x, y coordinates."""
    global _reducer
    X = np.array([np.asarray(e, dtype=np.float32) for e in embeddings])
    _reducer = umap.UMAP(
        n_components=2,
        n_neighbors=min(10, len(X) - 1),
        min_dist=0.3,
        metric="cosine",
        random_state=42,
    ).fit(X)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(_reducer, MODEL_PATH)
    return _reducer.embedding_


def transform(embedding) -> tuple[float, float]:
    """Place ONE new idea on the existing map. Nobody else moves."""
    global _reducer
    if _reducer is None:
        _reducer = joblib.load(MODEL_PATH)
    vec = np.asarray(embedding, dtype=np.float32).reshape(1, -1)
    x, y = _reducer.transform(vec)[0]
    return float(x), float(y)