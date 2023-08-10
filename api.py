import requests
import json

class RealEstateAPI:
    def __init__(self):
        self.base_url = "http://api.realestate.co.nz/"

    def pull_data(self):
        # Make a GET request to the API
        response = requests.get(self.base_url)

        # Parse the JSON response
        data = json.loads(response.text)

        return data
