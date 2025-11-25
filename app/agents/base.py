import os
import asyncio
from groq import Groq

# Load Groq API key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def _call_groq(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ Your supported model
        messages=[
            {
                "role": "system",
                "content": "You are an expert code reviewer. ALWAYS respond only with pure JSON array. No explanations outside JSON."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

async def ask_llm(prompt: str):
    try:
        return await asyncio.to_thread(_call_groq, prompt)
    except Exception as e:
        print("LLM ERROR:", e)
        return "[]"
