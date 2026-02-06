import requests
import os

class WeatherTool:
    def get_weather(self, city: str):
        api_key = os.getenv("WEATHER_API_KEY")
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"]
        }
