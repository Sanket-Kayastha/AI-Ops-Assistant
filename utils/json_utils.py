import json
import re

def extract_json(text: str) -> dict:
    
    if not text or not text.strip():
        raise ValueError("Empty LLM response")

    text = re.sub(r"```json|```", "", text).strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError(f"No JSON found in response:\n{text}")

    return json.loads(match.group())
