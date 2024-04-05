from augment_rank import rank_locations, rank_nature


def test_rank_locations_with_ties():
    incidents = [
        {"location": "Location A"},
        {"location": "Location A"},
        {"location": "Location B"}
    ]
    rank_locations(incidents)
    for incident in incidents:
        if incident["location"] == "Location A":
            assert incident["location_rank"] == 1
        else:
            assert incident["location_rank"] == 3

def test_rank_nature_without_ties():
    incidents = [
        {"nature": "Nature A"},
        {"nature": "Nature A"},
        {"nature": "Nature C"}
    ]
    rank_nature(incidents)
    for incident in incidents:
        if incident["nature"] == "Nature A":
            assert incident["nature_rank"] == 1
        else:
            assert incident["nature_rank"] == 3
