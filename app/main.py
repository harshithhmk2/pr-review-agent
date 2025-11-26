from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import asyncio

from app.agents.parser import parse_unified_diff
from app.agents.logic import analyze_logic
from app.agents.security import analyze_security
from app.agents.performance import analyze_performance
from app.agents.synthesizer import synthesize
from app.github import fetch_pr_diff

app = FastAPI()

class DiffInput(BaseModel):
    diff: str

# Redirect root to Swagger UI
@app.get("/", include_in_schema=False)
def home():
    return RedirectResponse(url="/docs")

@app.post("/review-diff")
async def review_diff(data: DiffInput):
    parsed = parse_unified_diff(data.diff)

    results = await asyncio.gather(
        analyze_logic(parsed),
        analyze_security(parsed),
        analyze_performance(parsed)
    )

    return synthesize(results)

@app.get("/review-pr")
async def review_pr(owner: str, repo: str, pr: int, token: str | None = None):
    diff = await fetch_pr_diff(owner, repo, pr, token)

    parsed = parse_unified_diff(diff)

    logic = await analyze_logic(parsed)
    security = await analyze_security(parsed)
    performance = await analyze_performance(parsed)

    final = synthesize([logic, security, performance])

    return final
