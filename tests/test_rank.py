from augment_rank import rank_locations, rank_nature


def test_rank_nature_with_varied_frequencies_and_ties():
    incidents = [
        {"nature": "Nature A"},  # Expected rank: 1 (Most frequent) A:3,E:2,C:2,B:1,D:1,F:1,G:1
        {"nature": "Nature A"},  # Expected rank: 1
        {"nature": "Nature A"},  # Expected rank: 1
        {"nature": "Nature B"},  # Expected rank: 4
        {"nature": "Nature C"},  # Expected rank: 5 (Tied)
        {"nature": "Nature C"},  # Expected rank: 5 (Tied)
        {"nature": "Nature D"},  # Expected rank: 7
        {"nature": "Nature E"},  # Expected rank: 8 (Tied)
        {"nature": "Nature E"},  # Expected rank: 8 (Tied)
        {"nature": "Nature F"},  # Expected rank: 10 (Tied)
        {"nature": "Nature G"},  # Expected rank: 11
    ]
    rank_nature(incidents)
    expected_ranks = {
        "Nature A": 1,
        "Nature B": 4,
        "Nature C": 2,
        "Nature D": 4,
        "Nature E": 2,
        "Nature F": 4,
        "Nature G": 4,
    }
    for incident in incidents:
        assert incident["nature_rank"] == expected_ranks[incident["nature"]]

def test_rank_location_with_varied_frequencies_and_ties():
    incidents = [
        {"location": "Location A"},  # Expected rank: 1 (Most frequent) A:3,E:2,C:2,B:1,D:1,F:1,G:1
        {"location": "Location A"},  # Expected rank: 1
        {"location": "Location A"},  # Expected rank: 1
        {"location": "Location B"},  # Expected rank: 4
        {"location": "Location C"},  # Expected rank: 5 (Tied)
        {"location": "Location C"},  # Expected rank: 5 (Tied)
        {"location": "Location D"},  # Expected rank: 7
        {"location": "Location E"},  # Expected rank: 8 (Tied)
        {"location": "Location E"},  # Expected rank: 8 (Tied)
        {"location": "Location F"},  # Expected rank: 10 (Tied)
        {"location": "Location G"},  # Expected rank: 11
    ]
    rank_locations(incidents)
    expected_ranks = {
        "Location A": 1,
        "Location B": 4,
        "Location C": 2,
        "Location D": 4,
        "Location E": 2,
        "Location F": 4,
        "Location G": 4,
    }
    for incident in incidents:
        assert incident["location_rank"] == expected_ranks[incident["location"]]