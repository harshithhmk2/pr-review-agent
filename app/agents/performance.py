from .base import ask_llm
import json

async def analyze_performance(parsed):
    prompt = f"""
You are a performance optimization expert.

Analyze the following code diff ONLY for performance and efficiency problems:

{parsed}

Return ONLY a JSON array with objects like:

[
  {{
    "file": "app.py",
    "line": 22,
    "type": "performance",
    "severity": "medium",
    "message": "Performance issue description",
    "suggestion": "Fix suggestion"
  }}
]

If no issues are found, return: []
"""

    output = await ask_llm(prompt)

    try:
        return json.loads(output)
    except:
        return []
