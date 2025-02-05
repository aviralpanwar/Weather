import requests
from datetime import datetime

API_KEY = 'a1e60d4d8a393886f2d3271f8dea678e'
LOCATION = 'San Antonio,US'
BASE_URL = 'http://api.openweathermap.org/data/2.5/'

def get_weather_data(endpoint, params):
    url = BASE_URL + endpoint
    params['appid'] = API_KEY
    response = requests.get(url, params=params)
    return response.json()

def display_current_weather(data):
    main = data['main']
    weather = data['weather'][0]
    temp = main['temp']
    description = weather['description']
    print(f"Current Weather in San Antonio, TX:")
    print(f"Temperature: {temp}°F")
    print(f"Condition: {description.capitalize()}")

def display_forecast(data):
    print("\n7-Day Forecast:")
    # Grouping the forecast by day
    forecast_data = {}
    for entry in data['list']:
        dt = datetime.fromtimestamp(entry['dt'])
        day = dt.strftime('%Y-%m-%d')  # Get the date only (no time)
        
        # Group by date
        if day not in forecast_data:
            forecast_data[day] = {
                'temp_max': entry['main']['temp_max'],
                'temp_min': entry['main']['temp_min'],
                'description': entry['weather'][0]['description']
            }
        else:
            forecast_data[day]['temp_max'] = max(forecast_data[day]['temp_max'], entry['main']['temp_max'])
            forecast_data[day]['temp_min'] = min(forecast_data[day]['temp_min'], entry['main']['temp_min'])

    # Display the forecast for the next 7 days
    for day, forecast in forecast_data.items():
        dt = datetime.strptime(day, '%Y-%m-%d')
        temp_max = forecast['temp_max']
        temp_min = forecast['temp_min']
        description = forecast['description']
        print(f"{dt.strftime('%A, %B %d')}: Max Temp: {temp_max}°F, Min Temp: {temp_min}°F, {description.capitalize()}")

def main():
    # Get current weather
    current_params = {'q': LOCATION, 'units': 'imperial'}
    current_weather = get_weather_data('weather', current_params)
    display_current_weather(current_weather)

    # Get 5-day forecast (with 3-hour intervals)
    forecast_params = {'q': LOCATION, 'units': 'imperial'}
    forecast = get_weather_data('forecast', forecast_params)
    display_forecast(forecast)

if __name__ == '__main__':
    main()
