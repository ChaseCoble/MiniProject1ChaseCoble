# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 1 Tests
# U
import os
import pytest
from src.client import PracticeHubClient

def test_get_posts_return_single_post(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        "id": 42,
        "title": "Test Post",
        "body": "Test body",
        "tags": ["test"],
        "author_id": 1,
        "author_name": "testuser",
        "created_at": "2026-09-03T14:45:17.968Z",
        "updated_at": "2026-09-03T14:45:17.968Z",
        "attachments": []
    }
    mock_response.raise_for_status.return_value = None
    mock_get = mocker.patch("requests.get", return_value=mock_response)
    client = PracticeHubClient(base_url="https://practice.fhsucyber.com", token="fake-token")
    result = client.get_post(42)

    mock_get.assert_called_once_with(
        "https://practice.fhsucyber.com/api/v1/posts/42",
        headers=client.headers
    )
    assert result["id"] == 42
    assert result["title"] == "Test Post"
