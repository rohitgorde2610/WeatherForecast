# api.py

import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():                 #Fetches weather data from the API and returns it as a JSON object.
    response = requests.get(API_URL)
    data = response.json()
    return data

def get_data_by_date(data, date):       #Filters and returns the forecast data for a specific date from the weather data.
    for forecast in data['list']:
        if forecast['dt_txt'] == date:
            return forecast