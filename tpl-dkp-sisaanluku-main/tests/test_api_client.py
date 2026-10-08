import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from client.api_client import fetch_data

@patch('client.api_client.requests.get')
def test_fetch_data_success(mock_get):
    # Mock successful response
    mock_response = MagicMock()
    mock_response.ok = True
    mock_response.json.return_value = [{'id': 1, 'title': 'Test'}]
    mock_get.return_value = mock_response

    result = fetch_data('https://example.com')
    assert result == [{'id': 1, 'title': 'Test'}]
    mock_get.assert_called_once_with('https://example.com')

@patch('client.api_client.requests.get')
def test_fetch_data_failure(mock_get):
    # Mock failed response
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("404 Client Error")
    mock_get.return_value = mock_response

    result = fetch_data('https://example.com')
    assert result is None

@patch('client.api_client.requests.get')
def test_fetch_data_exception(mock_get):
    # Mock exception during request
    mock_get.side_effect = Exception('Network error')

    result = fetch_data('https://example.com')
    assert result is None