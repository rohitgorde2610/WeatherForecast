# weather_info.py
def get_temperature(data):      #Extracts and returns the temperature from the weather data.
    return data['main']['temp']

def get_wind_speed(data):       #Extracts and returns the wind speed from the weather data.
    return data['wind']['speed']

def get_pressure(data):         #Extracts and returns the pressure from the weather data.
    return data['main']['pressure']
