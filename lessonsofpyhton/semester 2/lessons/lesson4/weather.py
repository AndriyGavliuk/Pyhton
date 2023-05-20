import requests


def parse_weather(city: str):
    api_key = "9a6642e9c33f5f759eda3f77a9c1dd8e"
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}"
    response = requests.get(url)

    return response.json()


if __name__ == "__main__":
    print(parse_weather("Kyiv"))
