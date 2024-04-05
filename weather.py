from datetime import datetime
import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import datetime

def augmentColummnWiseDataWithWeather(date_time_str, geocode):

    # hardcoding the latitude and longitude to center of Norman, OK
    if geocode == ["Unknown"]:
        latitude = 35.2226
        longitude = -97.4395
    else:
        latitude = geocode[0]
        longitude = geocode[1]
    

    
   # Setup caching and retry for requests
    cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    incident_datetime = datetime.strptime(date_time_str, "%m/%d/%Y %H:%M")

    # Extract the hour from the adjusted incident datetime
    incident_hour = incident_datetime.hour

    # Format date for the API request
    date = incident_datetime.strftime("%Y-%m-%d")

    # Set up API request parameters
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": date,
        "end_date": date,
        "hourly": ["weather_code"],
        "timezone": "auto"
    }

    # Fetch weather data
    responses = openmeteo.weather_api("https://archive-api.open-meteo.com/v1/archive", params=params)

    # Assuming the response structure matches the expected format
    if responses:
        response = responses[0]
        # Directly use incident_hour as index if weather_code array is hourly
        weather_codes = response.Hourly().Variables(0).ValuesAsNumpy()
        if 0 <= incident_hour < len(weather_codes):
            weather_code = weather_codes[incident_hour]
            formatted_weather_code = f"{int(weather_code):02d}"
            return formatted_weather_code
        else:
            return "Unknown"  # Handle cases where incident_hour is out of range
    return "Unknown"


# Fetch weather data in parallel
def fetch_weather_for_incident(incident):
        geocode = incident["geocode"]
        date_time_str = incident["date_time"]
        weather_code = augmentColummnWiseDataWithWeather(date_time_str, geocode)
        return weather_code