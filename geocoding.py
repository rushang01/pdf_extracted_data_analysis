import requests

API_KEY = "AIzaSyB06Lv6QxHs9EfcbhPPDEUj8XkibwIHA-4"

GOOGLE_MAPS_API_URL = f"https://maps.googleapis.com/maps/api/geocode/json?key={API_KEY}"

geolocation_cache = {}

def get_geocode_from_address(address):  
    global geolocation_cache

    if address in geolocation_cache:
        return geolocation_cache[address]
    
    # Set up API request parameters

    params = {
        "address": address,
        "key": API_KEY,
        "sensor": "false"
    }

    response = requests.get(GOOGLE_MAPS_API_URL, params=params)

    if response.status_code == 200: 
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return [location['lat'], location['lng']]
        else:
            pass
    else:
        pass

    geolocation_cache[address] = ["Unknown"]
    return ["Unknown"]
