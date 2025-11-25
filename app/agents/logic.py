from .base import ask_llm
import json

async def analyze_logic(parsed):
    prompt = f"""
You are an expert software engineer.

Analyze the following code diff for LOGIC ERRORS ONLY:

{parsed}

Return ONLY a JSON array with objects like this:

[
  {{
    "file": "app.py",
    "line": 12,
    "type": "logic",
    "severity": "high",
    "message": "Bug explanation",
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
