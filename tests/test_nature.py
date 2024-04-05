import pytest
from assignment2 import rank_nature

@pytest.mark.parametrize("incidents, expected_ranks", [
    ([{"nature": "Theft"}, {"nature": "Theft"}, {"nature": "Assault"}], {"Theft": 1, "Assault": 2}),  # Example case with expected ranks
    # Add more test cases as needed
])
def test_nature_ranking(incidents, expected_ranks):
    rank_nature(incidents)
    for incident in incidents:
        assert incident["nature_rank"] == expected_ranks[incident["nature"]]
