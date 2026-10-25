SYSTEM = (
    "You help students find hackathon teammates. Be specific and concrete. "
    "Refer to details from both projects. No generic filler."
)

def explain_prompt(a: dict, b: dict) -> str:
    return f"""{a['name']}'s project: {a['text']}
{b['name']}'s project: {b['text']}

In 2-3 sentences addressed to {a['name']}, explain where these two projects
overlap, how they differ, and one concrete thing they could build together."""