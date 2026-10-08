import pytest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os
import json

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import main

@patch('main.pd.DataFrame')
@patch('main.fetch_data')
@patch('main.validate_items')
def test_main_success(mock_validate, mock_fetch, mock_df_class):
    # Mock data
    mock_data = [{'id': 1, 'title': 'Test'}]
    mock_fetch.return_value = mock_data
    # validate_items doesn't return, but raises if invalid, so no need for return_value
    
    # Mock DataFrame instance
    mock_df_instance = MagicMock()
    mock_df_class.return_value = mock_df_instance

    main()

    # Check calls
    mock_fetch.assert_called_once_with("https://jsonplaceholder.typicode.com/posts")
    mock_validate.assert_called_once_with(mock_data)
    mock_df_class.assert_called_once_with(mock_data)
    mock_df_instance.to_json.assert_called_once_with("data/posts.json")

@patch('main.fetch_data')
@patch('main.validate_items')
def test_main_fetch_fails(mock_validate, mock_fetch):
    mock_fetch.return_value = None

    main()

    mock_fetch.assert_called_once()
    mock_validate.assert_not_called()
