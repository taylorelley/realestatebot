import requests

class APIHandler:
    """Class to handle interactions with the realestate.co.nz API."""

    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get_properties(self):
        """Method to get all properties from the API."""
        response = requests.get(self.base_url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return None
