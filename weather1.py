import requests
from datetime import datetime

API_KEY = 'ec8172034c6e35542b83a5fe750b7417'  # Replace with your OpenWeatherMap API key
LAT, LON = 29.4241, -98.4936  # Coordinates for San Antonio, TX
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall'

def get_weather_data():
    """Fetch weather data using One Call API."""
    params = {
        'lat': LAT,
        'lon': LON,
        'exclude': 'minutely,hourly',
        'units': 'imperial',
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_current_weather(data):
    """Display current weather conditions."""
    current = data.get('current', {})
    temp = current.get('temp', 'N/A')
    description = current.get('weather', [{}])[0].get('description', 'N/A')

    print("\n\033[1mCurrent Weather in San Antonio, TX:\033[0m")
    print(f"Temperature: {temp}°F")
    print(f"Condition: {description.capitalize()}")

def display_forecast(data):
    """Display 7-day weather forecast."""
    print("\n\033[1m7-Day Forecast:\033[0m")
    for day in data.get('daily', []):
        dt = datetime.fromtimestamp(day.get('dt', 0))
        temp = day.get('temp', {}).get('day', 'N/A')
        description = day.get('weather', [{}])[0].get('description', 'N/A')
        print(f"{dt.strftime('%A, %B %d')}: {temp}°F, {description.capitalize()}")

def main():
    """Main function to fetch and display weather data."""
    data = get_weather_data()
    display_current_weather(data)
    display_forecast(data)

if __name__ == '__main__':
    main()
data = get_weather_data()
print("API Response:", data)
