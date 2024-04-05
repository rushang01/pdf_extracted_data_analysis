import pytest
from assignment2 import get_geocode_from_address, determine_side_of_town

@pytest.mark.parametrize("address, expected_lat_lon", [
    ("Norman,OK", [35.2225668, -97.4394777])
])
def test_geocode_fetching(address, expected_lat_lon):
    result = get_geocode_from_address(address)
    assert result == expected_lat_lon

@pytest.mark.parametrize("address, geocode, expected_direction", [
    ("3300 HEALTHPLEX PKWY", [35.2226, 97.4395], "N"),  # Example address and expected direction
    # Add more test cases as needed
])
def test_side_of_town_determination(address, geocode, expected_direction):
    result = determine_side_of_town(address, geocode)
    assert result == expected_direction
