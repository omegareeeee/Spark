
import json

from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def name_cluster(ideas: list[dict]) -> str | None:
    lines = "\n".join(
        f"- {i['title']}: {i['description'][:120]}" for i in ideas[:10]
    )

    prompt = (
        "These student project ideas were grouped together because they are related:\n"
        f"{lines}\n\n"
        "Give the group a theme name of 2-3 words that describes what they have in common. "
        "Use plain, specific words (e.g. 'Mental Wellness', 'Campus Sustainability'). "
        "Reply with the name only, no quotes or punctuation."
    )
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=20,
            temperature=0.3,   # low = consistent names
            messages=[{"role": "user", "content": prompt}],
        )
        return res.choices[0].message.content.strip().strip('"\'. ')
    except Exception:
        return None   # caller falls back to "Group 1", etc.

def explain_intersection(a: dict, b: dict) -> dict | None:
    """a, b = {"title": ..., "description": ...}. Returns {"title", "pitch", "why"} or None."""
    prompt = (
        "Two student project ideas from different areas:\n\n"
        f"A) {a['title']}: {a['description']}\n"
        f"B) {b['title']}: {b['description']}\n\n"
        "Invent ONE new project that genuinely combines both. "
        "Reply with JSON only, with these keys:\n"
        '"title": a short project name,\n'
        '"pitch": two sentences describing the combined project,\n'
        '"why": one sentence on what each original idea contributes.'
    )
    try:
        res = client.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=250,
            temperature=0.7,
            response_format={"type": "json_object"},
            messages=[{"role": "user", "content": prompt}],
        )
        data = json.loads(res.choices[0].message.content)
        return {k: str(data.get(k, "")) for k in ("title", "pitch", "why")}
    except Exception as e:
        print("explain_intersection failed:", repr(e))
        return None