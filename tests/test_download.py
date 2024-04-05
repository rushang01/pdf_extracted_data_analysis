import fitz  # PyMuPDF
import pytest
import os

from unittest.mock import patch, MagicMock
from io import BytesIO
import shutil

from assignment2 import extract_incidents_from_pdf, fetchincidents



@pytest.fixture
def mock_fetchincidents():
    with patch('urllib.request.urlopen') as mock_fetch:
        mock_response = BytesIO(b"PDF content")
        mock_fetch.return_value = MagicMock(read=MagicMock(return_value=mock_response.getvalue()))
        yield mock_fetch

def test_fetchincidents(mock_fetchincidents):
    url = "https://example.com/fake_url.pdf"
    expected_path = "/tmp/incident.pdf"

    actual_path = fetchincidents(url)

    assert actual_path == expected_path
    assert os.path.exists(actual_path)
    assert os.path.getsize(actual_path) > 0

    os.remove(actual_path)


def test_extract_incidents_from_pdf(tmp_path):
    pdf_path = tmp_path / "incident.pdf"
    # Path to your actual test PDF stored in the project's test directory
    test_pdf_path = 'tests/2024-01-07_daily_incident_summary.pdf'

    # Copy the test PDF to the temporary path used in the test
    shutil.copy(test_pdf_path, pdf_path)

    expected_incidents_subset = [      
        {"date_time": "1/7/2024 12:56", "incident_number": "2024-00001452", "location": "201 REED AVE", "nature": "Medical Call Pd Requested", "incident_ori": "OK0140200"},
        {"date_time": "1/7/2024 14:00", "incident_number": "2024-00000298", "location": "4913 LYON DR", "nature": "Falls", "incident_ori": "14005"}, 
        ]

    incidents = extract_incidents_from_pdf(str(pdf_path))
    print(incidents)
    for expected_incident in expected_incidents_subset:
        assert any(incident for incident in incidents if incident_matches(incident, expected_incident))

    

def incident_matches(incident, expected_incident):
    return all(incident[key] == expected_incident[key] for key in expected_incident.keys())





