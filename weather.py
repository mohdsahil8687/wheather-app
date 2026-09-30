import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather(city):

    url = (
        f"https://api.weatherapi.com/v1/current.json"
        f"?key={API_KEY}&q={city}&aqi=yes"
    )

    response = requests.get(url)

    data = response.json()

    return data