from sentence_transformers import SentenceTransformer

# Loads once when the app starts. The first run downloads ~90 MB.
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed(text: str) -> list[float]:
    """Text in, list of 384 numbers out."""
    return model.encode(text, normalize_embeddings=True).tolist()