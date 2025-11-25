from .base import ask_llm
import json

async def analyze_security(parsed):
    prompt = f"""
You are an application security expert.

Analyze the following code diff for SECURITY VULNERABILITIES ONLY:

{parsed}

Return ONLY a JSON array with objects like:

[
  {{
    "file": "app.py",
    "line": 5,
    "type": "security",
    "severity": "high",
    "message": "Issue description",
    "suggestion": "Fix suggestion"
  }}
]

If none are found, return: []
"""

    output = await ask_llm(prompt)

    try:
        return json.loads(output)
    except:
        return []
