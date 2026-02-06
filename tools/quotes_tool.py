import requests

class QuotesTool:
    def get_quote(self):
        url = "https://zenquotes.io/api/random"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()[0]
        return {
            "quote": data["q"],
            "author": data["a"]
        }
