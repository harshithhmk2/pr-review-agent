def synthesize(agent_outputs):
    combined = []

    for output in agent_outputs:
        if isinstance(output, list):
            combined.extend(output)

    severity_order = {"high": 0, "medium": 1, "low": 2}

    combined.sort(key=lambda c: severity_order.get(c.get("severity", "low"), 3))

    return {
        "total_comments": len(combined),
        "comments": combined
    }

