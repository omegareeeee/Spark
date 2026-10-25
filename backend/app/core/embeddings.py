import numpy as np
from openai import OpenAI
from app.core.config import EMBED_MODEL, EMBED_DIM

_client = OpenAI(timeout=20, max_retries=2)

def embed(texts: list[str]) -> np.ndarray:
    """Embed a batch of texts in one API call. Returns shape (len(texts), EMBED_DIM)."""
    if not texts:
        return np.empty((0, EMBED_DIM), dtype=np.float32)

    # Empty strings make the API error, so swap in a placeholder.
    cleaned = [t.strip() or "none" for t in texts]

    res = _client.embeddings.create(model=EMBED_MODEL, input=cleaned)
    vecs = np.array([d.embedding for d in res.data], dtype=np.float32)

    assert vecs.shape[1] == EMBED_DIM, (
        f"Embedding dim {vecs.shape[1]} != {EMBED_DIM}. "
        "Update EMBED_DIM and the Vector(DIM) columns."
    )
    return vecs