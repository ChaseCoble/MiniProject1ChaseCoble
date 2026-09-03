# INF601 - Advanced Programming in Python
# Chase Coble
# MIni Project 1

import os
import requests
from src.exceptions import BadTokenError, ForbiddenError, NotFoundError, MalformedError

BASE = "https://practice.fhsucyber.com"
TOKEN = os.environ.get("PRACTICE_API_TOKEN")


class PracticeHubClient:
    # Maps an HTTP status code to a (exception class, generic message) pair.
    # Messages are deliberately vague so a raw server response never leaks out.
    _ERRORS = {
        401: (BadTokenError, "Authentication failed: token missing, expired, or invalid."),
        403: (ForbiddenError, "Access denied: you do not have permission for this action."),
        404: (NotFoundError, "Not found: the requested resource does not exist."),
        422: (MalformedError, "Unprocessable request: the submitted data was invalid."),
    }

    def __init__(self, base_url, token):
        self.base = base_url.rstrip("/")
        self.headers = {"Authorization": f"Bearer {token}"}

    def _handle_response(self, resp):
        if resp.status_code in self._ERRORS:
            error_cls, message = self._ERRORS[resp.status_code]
            raise error_cls(message)
        resp.raise_for_status()
        if resp.status_code == 204 or not resp.content:
            return None
        return resp.json()

    def create_post(self, title, body="", tags=None):
        resp = requests.post(f"{self.base}/api/v1/posts", headers=self.headers,
                             json={"title": title, "body": body, "tags": tags or []})
        return self._handle_response(resp)

    def list_posts(self, mine=False, tag=None):
        params = {"mine": mine}
        if tag:
            params["tag"] = tag
        resp = requests.get(f"{self.base}/api/v1/posts", headers=self.headers, params=params)
        return self._handle_response(resp)

    # TODO (Mini Project 1): get_post, update_post, delete_post
    def get_post(self, post_id):
        if not isinstance(post_id, int):
            raise TypeError(f"post_id must be an int, got {type(post_id).__name__}")
        resp = requests.get(f"{self.base}/api/v1/posts/{post_id}", headers = self.headers)
        return self._handle_response(resp)

    def update_post(self, post_id, **fields):
        if not isinstance(post_id, int):
            raise TypeError(f"post_id must be an int, got {type(post_id).__name__}")
        resp = requests.patch(f"{self.base}/api/v1/posts/{post_id}",
                              json=fields, headers=self.headers)
        return self._handle_response(resp)

    def delete_post(self, post_id):
        if not isinstance(post_id, int):
            raise TypeError(f"post_id must be an int, got {type(post_id).__name__}")
        resp = requests.delete(f"{self.base}/api/v1/posts/{post_id}", headers=self.headers)
        self._handle_response(resp)
        return None

if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("PRACTICE_API_TOKEN is not set - see 'Set your token' in Week 2.")


    client = PracticeHubClient(BASE, TOKEN)

    everyone = client.list_posts()
    print(f"posts on the hub: {len(everyone)}")

    new_post = client.create_post("Week 3 lab", body="My first created post.")
    print(f"created post {new_post['id']}: {new_post['title']}")

    print(f"posts that are mine: {len(client.list_posts(mine=True))}")
