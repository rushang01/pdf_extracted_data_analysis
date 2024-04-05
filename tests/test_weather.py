from weather import fetch_weather_for_incident


def test_fetch_weather_for_incident_daytime():
    incident = {"date_time": "04/01/2024 14:00", "geocode": [35.2226, -97.4395]}
    # This test requires mocking the response from OpenMeteo or simulating it.
    expected_weather_code = "51"  # Assume clear sky code for simplicity
    assert fetch_weather_for_incident(incident) == expected_weather_code

def test_fetch_weather_for_incident_night():
    incident = {"date_time": "04/01/2024 02:00", "geocode": [35.2226, -97.4395]}
    # This test requires mocking the response from OpenMeteo or simulating it.
    expected_weather_code = "01"  # Assume night clear sky code for simplicity
    assert fetch_weather_for_incident(incident) == expected_weather_code