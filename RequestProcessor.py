import requests

from CheckEnvs import check_env

class RemoteAPICallFailed(Exception):
    pass

class RequestProcessor:
    """
    This class responsible for interaction with the API.
    """
    def __init__(self):
        self.base_url = check_env('BASE_REQUEST_URL')
        self.api_key = check_env('API_KEY')
    
    def make_request(self, url):
        """
        Make a request with the base url + passed in url.
        """
        # Add API key to headers for authentication.
        headers = {'x-api-key': self.api_key}

        # Build the complete URL with base + passed in URL.
        full_url = f"{self.base_url}{url}"

        # Verify we got an okay status code and pass the response back.
        check_results = requests.get(full_url, headers=headers)

        if check_results.status_code == requests.codes.ok:
            return check_results
        else:
            raise RemoteAPICallFailed(f"Request failed, Status Code : {check_results.status_code}")