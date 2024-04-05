import math


def calculate_bearing(center_lat, center_lon, lat, lon):
    # Convert from degrees to radians
    center_lat, center_lon, lat, lon = map(math.radians, [center_lat, center_lon, lat, lon])

    delta_lon = lon - center_lon
    x = math.cos(lat) * math.sin(delta_lon)
    y = math.cos(center_lat) * math.sin(lat) - (math.sin(center_lat) * math.cos(lat) * math.cos(delta_lon))
    bearing = math.atan2(x, y)
    
    # Convert from radians to degrees and normalize
    bearing = (math.degrees(bearing) + 360) % 360
    
    return bearing

def get_direction_from_bearing(bearing):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(bearing / 45) % 8
    return directions[index]




def determine_side_of_town(address, geocode, center=(35.220833, -97.443611)):
    if geocode != ["Unknown"]:
        lat = geocode[0]
        lon = geocode[1]
        bearing = calculate_bearing(center[0], center[1], lat, lon)
        direction = get_direction_from_bearing(bearing)
        return direction
    
    return "Unknown"