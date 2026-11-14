import requests
import json

response = requests.get("https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&units=imperial&appid=2cd9e319d6835a99f4ac86d04c7cc659&lang=en")

lat = 33.44
lon = -94.04
units = "imperial"
appid = "2cd9e319d6835a99f4ac86d04c7cc659"
lang = "en"



if response.status_code == 200:
    
    weather = response.json()
    
    print(f"Lattitiude: {weather['lat']}")
    print(f"Longitude: {weather['lon']}")
    print(f"Timezone: {weather['timezone']}")
    print(f"Temperature: {weather['current']['temp']}")
    print(f"Current weather: {weather['current']['weather']}")

else:
    print("Error: API Data unretrievable.", response.status_code)
