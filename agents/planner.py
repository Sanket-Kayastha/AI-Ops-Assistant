from llm.llm_client import call_llm
from utils.json_utils import extract_json

class PlannerAgent:
    def plan(self, user_task: str) -> dict:
        prompt = f"""
            You are a Planner Agent.

            Convert the user task into a STRICT JSON plan.

            Rules:
            - Output ONLY valid JSON
            - No explanations
            - No markdown
            - No text outside JSON

            JSON format:
            {{
            "steps": [
                {{
                "task": "description",
                "tool": "WeatherTool or QuotesTool"
                }}
            ]
            }}

            User task:
            {user_task}
            """
        response = call_llm(prompt)
        return extract_json(response)
