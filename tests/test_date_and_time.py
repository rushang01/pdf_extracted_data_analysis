import pytest
from datetime import datetime
from assignment2 import augmentColummnWiseDataWithDateAndTime

@pytest.mark.parametrize("incident, expected_day, expected_hour", [
    ({"date_time": "03/15/2024 14:00"}, 6, 14),  # Testing for correct day and hour extraction
    # Add more test cases as needed
])
def test_time_extraction(incident, expected_day, expected_hour):
    augmentColummnWiseDataWithDateAndTime(incident)
    assert incident["day"] == expected_day
    assert incident["hour"] == str(expected_hour)
