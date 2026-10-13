import requests
from datetime import datetime
import pytz

# -----------------------------
# CONFIGURATION
# -----------------------------
# Get a free API key from https://openweathermap.org/api
API_KEY = "YOUR_API_KEY_HERE"

# List of countries/cities with their timezone and OpenWeatherMap city name
LOCATIONS = [
    {"city": "New York", "timezone": "America/New_York", "weather_city": "New York,US"},
    {"city": "London", "timezone": "Europe/London", "weather_city": "London,GB"},
    {"city": "Tokyo", "timezone": "Asia/Tokyo", "weather_city": "Tokyo,JP"},
    {"city": "Sydney", "timezone": "Australia/Sydney", "weather_city": "Sydney,AU"},
    {"city": "Mumbai", "timezone": "Asia/Kolkata", "weather_city": "Mumbai,IN"}
]

# -----------------------------
# FUNCTIONS
# -----------------------------
def get_local_time(timezone_str):
    """Return current local time and date for a given timezone."""
    try:
        tz = pytz.timezone(timezone_str)
        local_time = datetime.now(tz)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
        return f"Error getting time: {e}"

def get_weather(city_name):
    """Fetch weather data from OpenWeatherMap API."""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        weather_desc = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        return f"{weather_desc}, Temp: {temp}°C, Humidity: {humidity}%"
    except requests.exceptions.RequestException as e:
        return f"Weather API error: {e}"
    except KeyError:
        return "Invalid weather data received."

# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    print("Real World Time & Weather Conditions\n" + "-"*50)
    for loc in LOCATIONS:
        time_str = get_local_time(loc["timezone"])
        weather_str = get_weather(loc["weather_city"])
        print(f"{loc['city']}: {time_str} | {weather_str}")

if __name__ == "__main__":
    main()
