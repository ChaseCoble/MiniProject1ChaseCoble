# INF601 - Advanced Programming in Python
# Chase Coble
# Mini Project 1 Integration Tests
import os
import pytest
from src.client import PracticeHubClient
from src.exceptions import NotFoundError, ForbiddenError

TOKEN = os.environ.get("PRACTICE_API_TOKEN")

pytestmark = pytest.mark.skipif(
    not TOKEN, reason="PRACTICE_API_TOKEN not set — skipping live API integration tests"
)


@pytest.fixture
def live_client():
    return PracticeHubClient(base_url="https://practice.fhsucyber.com", token=TOKEN)


@pytest.fixture
def temp_post(live_client):
    """Creates a real post, yields it, deletes it afterward regardless of
    what the test did to it."""
    post = live_client.create_post(
        title="Integration Test Post",
        body="Created by integration test suite",
        tags=["integration-test"]
    )
    yield post
    try:
        live_client.delete_post(post["id"])
    except NotFoundError:
        pass


def test_create_post(live_client):
    post = live_client.create_post(
        title="Create Test", body="body text", tags=["test"]
    )
    assert post["title"] == "Create Test"
    assert post["id"] is not None
    live_client.delete_post(post["id"])

def test_read_post(live_client, temp_post):
    fetched = live_client.get_post(temp_post["id"])
    assert fetched["id"] == temp_post["id"]
    assert fetched["title"] == temp_post["title"]


def test_update_post(live_client, temp_post):
    updated = live_client.update_post(temp_post["id"], title="Updated Title")
    assert updated["title"] == "Updated Title"

    refetched = live_client.get_post(temp_post["id"])
    assert refetched["title"] == "Updated Title"


def test_delete_post_removes_it(live_client, temp_post):
    live_client.delete_post(temp_post["id"])

    with pytest.raises(NotFoundError):
        live_client.get_post(temp_post["id"])


def test_full_crud_cycle(live_client):
    created = live_client.create_post(
        title="Full Cycle Test", body="start", tags=["cycle"]
    )
    assert created["title"] == "Full Cycle Test"

    fetched = live_client.get_post(created["id"])
    assert fetched["id"] == created["id"]

    updated = live_client.update_post(created["id"], body="changed")
    assert updated["body"] == "changed"

    live_client.delete_post(created["id"])
    with pytest.raises(NotFoundError):
        live_client.get_post(created["id"])
