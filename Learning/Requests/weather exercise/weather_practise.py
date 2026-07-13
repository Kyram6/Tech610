from pprint import pprint
import requests

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather?"
latitude = 53.502443
longitude = -2.066219
with open("weather_api_key") as file:
    api_key = file.readline().strip() #secure


response = requests.get(WEATHER_ENDPOINT +f"lat={latitude}&lon={longitude}&appid={api_key}&units=metric")

print(response.status_code)

if response.status_code == 200:
    weather = response.json()
    pprint(weather)

