import requests

class APIClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.token = self.login(username, password)
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def login(self, username, password):
        r = requests.post(
            f"{self.base_url}/login",
            auth=(username, password)
        )
        r.raise_for_status()
        return r.json()["token"]

    def get(self, endpoint):
        r = requests.get(self.base_url + endpoint, headers=self.headers)
        r.raise_for_status()
        return r.json()

    def put(self, endpoint, payload):
        r = requests.put(
            self.base_url + endpoint,
            headers=self.headers,
            json=payload
        )
        r.raise_for_status()
        return r.json()
