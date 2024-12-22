import requests
import logging

logging.basicConfig(level=logging.INFO)

class Client:
    def __init__(self, token: str):
        self.base_url: str = "https://discord.com/api/v10"
        self.token = token
        self.headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
    
    def get(self, endpoint: str) -> dict | None:
        """Get result to request on url
        endpoint -> endpoint url:
            /users/@me
        """
        url = f"{self.base_url}{endpoint}"
        logging.info(f"GET - {url}")
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def post(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}{endpoint}"
        logging.info(f"POST URL - {url} - DATA - {data}")
        response = requests.post(url, headers=self.headers, json=data)
    
    def _handler_response(self, response: requests.Response):
        if not response.ok:
            logging.error(f"HTTP - {response.status_code} - {response.text}")