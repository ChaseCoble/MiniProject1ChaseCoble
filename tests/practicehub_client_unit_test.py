# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 1 Unit Tests

import os
import pytest
from src.client import PracticeHubClient

@pytest.fixture
def client():
    return PracticeHubClient(base_url="https://practice.fhsucyber.com", token="fake-token")

@pytest.fixture
def sample_post():
    return {
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
@pytest.fixture
def mock_response(mocker):
    def _make(json_data, status_code=200):
        resp = mocker.Mock()
        resp.json.return_value = json_data
        resp.status_code = status_code
        resp.raise_for_status.return_value = None
        return resp
    return _make
#Single Post Get
def test_return_single_post(client, mock_response, sample_post, mocker):
    resp = mock_response(sample_post)
    mock_get = mocker.patch("requests.get", return_value=resp)
    result = client.get_post(42)

    mock_get.assert_called_once_with(
        "https://practice.fhsucyber.com/api/v1/posts/42",
        headers=client.headers
    )
    assert result == sample_post
#Single Post update
def test_update_post_single_field(client, mock_response, sample_post, mocker):
    resp = mock_response(sample_post)
    mock_patch = mocker.patch("requests.patch", return_value=resp)

    client.update_post(42, title="New title")

    mock_patch.assert_called_once_with(
        "https://practice.fhsucyber.com/api/v1/posts/42",
        json={"title": "New title"},
        headers=client.headers
    )

def test_update_post_multiple_fields(client, mock_response, sample_post, mocker):
    resp = mock_response(sample_post)
    mock_patch = mocker.patch("requests.patch", return_value=resp)

    client.update_post(42, title="New title", tags=["updated"])

    mock_patch.assert_called_once_with(
        "https://practice.fhsucyber.com/api/v1/posts/42",
        json={"title": "New title", "tags": ["updated"]},
        headers=client.headers
    )

def test_update_post_no_fields_sends_empty_payload(client, mock_response, sample_post, mocker):
    resp = mock_response(sample_post)
    mock_patch = mocker.patch("requests.patch", return_value=resp)

    client.update_post(42)

    mock_patch.assert_called_once_with(
        "https://practice.fhsucyber.com/api/v1/posts/42",
        json={},
        headers=client.headers
    )

