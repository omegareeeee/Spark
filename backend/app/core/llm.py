import hashlib
import logging
from openai import OpenAI
from app.core.config import LLM_MODEL
from app.db.session import SessionLocal
from app.models import LLMCache

log = logging.getLogger(__name__)
_client = OpenAI(timeout=30, max_retries=2)

FALLBACK = "We couldn't generate this right now. Please try again in a moment."

def _key(prompt: str, system: str, max_tokens: int) -> str:
    raw = f"{LLM_MODEL}|{max_tokens}|{system}|{prompt}"
    return hashlib.sha256(raw.encode()).hexdigest()

def complete(prompt: str, system: str = "", max_tokens: int = 400,
             fallback: str = FALLBACK) -> str:
    """OpenAI chat call with a DB-backed cache. Same inputs return instantly."""
    key = _key(prompt, system, max_tokens)

    with SessionLocal() as s:
        hit = s.get(LLMCache, key)
        if hit:
            return hit.response

    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    try:
        res = _client.chat.completions.create(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=max_tokens,
        )
        text = (res.choices[0].message.content or "").strip()
    except Exception as e:
        log.warning("LLM call failed: %s", e)
        return fallback

    with SessionLocal() as s:
        s.merge(LLMCache(key=key, response=text))
        s.commit()
    return text