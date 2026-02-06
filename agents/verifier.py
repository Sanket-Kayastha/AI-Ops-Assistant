from llm.llm_client import call_llm
from utils.json_utils import extract_json
import json

class VerifierAgent:
    def verify(self, data: dict) -> dict:
        prompt = f"""
            You are a Verifier Agent.

            Clean, validate, and format the following data.
            Return ONLY valid JSON.
            No explanations.

            Input data:
            {json.dumps(data, indent=2)}
            """
        response = call_llm(prompt)
        return extract_json(response)
