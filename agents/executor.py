from tools.weather_tool import WeatherTool
from tools.quotes_tool import QuotesTool

class ExecutorAgent:
    def execute(self, plan: dict) -> dict:
        results = {}

        for step in plan["steps"]:
            tool = step["tool"]
            task = step["task"]

            if tool == "WeatherTool":
                city = task.split("for")[-1].strip()
                results["weather"] = WeatherTool().get_weather(city)

            elif tool == "QuotesTool":
                results["quote"] = QuotesTool().get_quote()

            

        return results
