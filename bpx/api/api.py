import requests
from bpx.authentication.signing_requests import SigningRequests
from tools.utils import Singleton


@Singleton
class Api(SigningRequests):
    def __init__(self, window: int = 5000) -> None:
        super().__init__(window)

    def get(self, url: str, instruction: str = "", parameters: dict = {}) -> tuple:
        headers = self.get_headers(instruction, parameters)
        response = requests.get(
            url,
            headers=headers,
            params=parameters,
        )
        status_code = response.status_code
        if status_code == 200:
            return (response.json(), status_code)
        else:
            return False

    def post(self, url: str, instruction: str = "", parameters: dict = {}) -> tuple:
        headers = self.get_headers(instruction, parameters)
        response = requests.post(
            url,
            headers=headers,
            json=parameters,
        )
        status_code = response.status_code
        if status_code == 200:
            if "withdrawals" not in url:

                return (response.json(), status_code)
            else:
                return ("OK", status_code)
        else:
            return False

    def delete(self, url: str, instruction: str = "", parameters: dict = {}) -> tuple:
        headers = self.get_headers(instruction, parameters)
        response = requests.delete(
            url,
            headers=headers,
            json=parameters,
        )
        status_code = response.status_code
        if status_code == 200:
            return (response.json(), status_code)
        else:
            return False
