
from openai import OpenAI

client = OpenAI()

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